def pytest_funcarg__testdir(request):
    testdir = request.getfuncargvalue('testdir')
    testdir.makeini('[pytest]\ncodechecks = pyflakes')
    return testdir


def test_pyflakes_finds_name_error(testdir):
    testdir.makepyfile('''
        def tesdt_a():
            pass
        def b():
            abc
        ''')
    #XXX: bad hack cause i fail to disable the pep8 checker
    out = testdir.runpytest('--tb=short', '-k', 'flakes', '-v')
    out.stdout.fnmatch_lines([
        '*abc*',
        '*1 failed*',
        ])


def test_reportinfo_verbose(testdir):
    testdir.makepyfile('''
        def xyz():
            pass
        ''')
    out = testdir.runpytest('-v')
    out.stdout.fnmatch_lines([
        '*test_reportinfo_verbose.py:0: codecheck pyflakes PASSED',
        ])
