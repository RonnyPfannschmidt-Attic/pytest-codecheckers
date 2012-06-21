import py

import pkg_resources


class FoundErrors(Exception):
    def __init__(self, count, out, err):
        self.count = count
        self.out = out
        self.err = err


class PyCodeCheckItem(py.test.collect.Item):
    def __init__(self, ep, parent):
        py.test.collect.Item.__init__(self, ep.name, parent)
        main = py.path.local()
        self.filename = main.bestrelpath(self.fspath)
        self._ep = ep

    def runtest(self):
        check = self._ep.load().check_file
        call = py.io.StdCapture.call

        found_errors, out, err = call(check, self.fspath, self.filename)
        if found_errors:
            raise FoundErrors(FoundErrors, out, err)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(FoundErrors):
            return excinfo.value.out
        return super(PyCodeCheckItem, self).repr_failure(excinfo)

    def reportinfo(self):
        return (self.fspath, -1, "codecheck " + self._ep.name)


class PyCheckerCollector(py.test.collect.File):
    def __init__(self, path, parent):
        super(PyCheckerCollector, self).__init__(path, parent)
        self.name += '[code-check]'

    def collect(self):
        if self.config.option.no_codechecks:
            return []
        checkers = self.config.getini('codechecks')
        entrypoints = pkg_resources.iter_entry_points('codechecker')
        wanted = (ep for ep in entrypoints if ep.name in checkers)
        return [PyCodeCheckItem(wep, self) for wep in wanted]


def pytest_collect_file(path, parent):
    if path.ext == '.py':
        return PyCheckerCollector(path, parent)


def pytest_addoption(parser):
    parser.addini('codechecks', type='args',
                  help='listings of the codechecks to use',
                  default=['pep8', 'pyflakes'])
    parser.addoption('--no-codechecks', action='store_true')
