def test_pyflakes_finds_name_error(testdir):
    f = testdir.makepyfile('''
        def tesdt_a():
            pass
        def b():
            abc
        ''')
    f.write(f.read() + '\n') #XXX: bad hack cause i fail to disable the pep8 checker
    out = testdir.runpytest('--tb=short', '-k', 'flakes')
    out.stdout.fnmatch_lines([
        '*1 failed*',
        ])
