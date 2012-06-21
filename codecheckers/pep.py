import pep8


def check_file(path, filename):
    checker = pep8.Checker(filename, path.readlines(),
                           show_source=True,
                           repeat=True)
    return checker.check_all()
