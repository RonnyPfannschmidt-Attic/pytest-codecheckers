import py

import pkg_resources


class PyCodeCheckItem(py.test.collect.Item):
    def __init__(self, ep, parent):
        py.test.collect.Item.__init__(self, ep.name, parent)
        self._ep = ep

    def runtest(self):
        c = py.io.StdCapture()
        mod = self._ep.load()
        try:
            found_errors, out, err = c.call(mod.check_file, self.fspath)
            self.out, self.err = out, err
        except:
            found_errors = True
            self.info = py.code.ExceptionInfo()
        assert not found_errors

    def repr_failure(self, exc_info):
        try:
            return self.out
        except AttributeError:
            #XXX: internal error ?!
            return super(PyCodeCheckItem, self).repr_failure(self.info)

    def reportinfo(self):
        return (self.fspath, -1, "codecheck %s" % self._ep.name)


class PyCheckerCollector(py.test.collect.File):
    def __init__(self, path, parent):
        super(PyCheckerCollector, self).__init__(path, parent)
        self.name += '[code-check]'

    def collect(self):
        if self.config.option.no_codechecks:
            return []
        checkers = self.config.getini('codechecks')
        entrypoints = pkg_resources.iter_entry_points('codechecker')
        #XXX: list wanted checkers we didnt get
        return [PyCodeCheckItem(ep, self) for ep in entrypoints if ep.name in checkers]


def pytest_collect_file(path, parent):
    if path.ext == '.py':
        return PyCheckerCollector(path, parent)


def pytest_addoption(parser):
    parser.addini('codechecks', type='args', help='listings of the codechecks to use')
    parser.addoption('--no-codechecks', action='store_true')
