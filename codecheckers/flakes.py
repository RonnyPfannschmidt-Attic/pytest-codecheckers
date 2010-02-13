from pyflakes.scripts.pyflakes import check as pyflakes_check

from pyflakes.checker import Binding, Assignment

def assignment_monkeypatched_init(self, name, source):
    Binding.__init__(self, name, source)
    if name == '__tracebackhide__':
        self.used = True

Assignment.__init__ = assignment_monkeypatched_init

def check_file(path):
    return pyflakes_check(path.read(), str(path))

