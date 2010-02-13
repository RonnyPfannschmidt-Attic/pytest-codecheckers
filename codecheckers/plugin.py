import py

import pkg_resources


class PyCodeCheckItem(py.test.collect.Item):
    def __init__(self, ep, parent):
        py.test.collect.Item.__init__(self, ep.name, parent)
        self._ep = ep

    def runtest(self):
        c = py.io.StdCapture()
        mod = self._ep.load()
        found_errors, out, err = c.call(mod.check_file, self.fspath)
        self.out, self.err = out, err
        assert not found_errors

    def repr_failure(self, exc_info):
        return self.out

    def reportinfo(self):
        return (self.fspath, -1, "codecheck %s" % self._ep.name)



class PyCheckerCollector(py.test.collect.File):
    def __init__(self, path, parent):
        super(PyCheckerCollector, self).__init__(path, parent)
        self.name += '[code-check]'

    def collect(self):
        entrypoints = pkg_resources.iter_entry_points('codechecker')
        return [PyCodeCheckItem(ep, self) for ep in entrypoints]


def pytest_collect_file(path, parent):
    if path.ext == '.py':
        return PyCheckerCollector(path, parent)

