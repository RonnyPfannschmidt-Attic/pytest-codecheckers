import py


def test_pyflakes_finds_name_error(testdir):
    testdir.makepyfile('''
        def tesdt_a():
            pass
        def b():
            abc
        ''')
    out = testdir.runpytest()
    out.stdout.fnmatch_lines([
        '*1 Failed*',
        ])
    print(out)
    assert 0
