import pytest


@pytest.fixture
def testdir(request):
    testdir = request.getfuncargvalue('testdir')
    testdir.makeini('[pytest]\ncodechecks = pep8')
    return testdir


def test_badcode(testdir):
    testdir.makepyfile('''
        def a():
            pass
        def b():
            pass''')
    out = testdir.runpytest('--tb=short', '-v')
    out.stdout.fnmatch_lines([
        '*lines*',
        '*1 failed*',
    ])


def test_goodcode(testdir):
    p = testdir.makepyfile('''
        def a():
            pass


        def b():
            pass

        ''')
    p.write(p.read() + '\n')
    out = testdir.runpytest('--tb=short', '-v')
    out.stdout.fnmatch_lines([
        '*1 passed*',
    ])
