def test_pyflakes_finds_name_error(testdir):
    f = testdir.makepyfile('''
        def tesdt_a():
            pass
        def b():
            abc
        ''')
    f.write(f.read() + '\n') #XXX: bad hack cause i fail to disable the pep8 checker
    out = testdir.runpytest('--tb=short', '-k', 'flakes', '-v')
    out.stdout.fnmatch_lines([
        '*abc*',
        '*1 failed*',
        ])

def test_reportinfo_verbose(testdir):
    f = testdir.makepyfile('''
        def xyz():
            pass
        ''')
    f.write(f.read() + '\n')
    out = testdir.runpytest('-v')
    out.stdout.fnmatch_lines([
        '*test_reportinfo_verbose.py: codecheck PASS',
        ])
