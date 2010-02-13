import py

import pkg_resources


class PyCodeCheckItem(py.test.collect.Item):
    def __init__(self, ep, parent):
        py.test.collect.Item.__init__(self, ep.name, parent)
        self._ep = ep

    def runtest(self):
        __tracebackhide__ = True
        mod = self._ep.load()
        mod.check_file(self.fspath)



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

