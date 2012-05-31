import sys
import pep8

class PyTestChecker(pep8.Checker):
    ignored_errors = 0
    def report_error(self, line_number, offset, text, check):
        #XXX: pep8 is a retarded module!
        if pep8.ignore_code(text[:4]):
            self.ignored_errors += 1
        pep8.Checker.report_error(self, line_number, offset, text, check)

def check_file(path, filename, io):
    oldio = sys.stdout, sys.stderr
    try:
        sys.stdout = sys.stderr = io
        pep8.process_options(['pep8',
            # ignore list taken from moin
            '--ignore=E202,E221,E222,E241,E301,E302,E401,E501,E701,W391,W601,W602',
            '--show-source',
            '--repeat',
            'dummy file',
            ])
        checker = PyTestChecker(filename, path.readlines())
        #XXX: bails out on death
        error_count = checker.check_all()
        ignored = checker.ignored_errors
        return max(error_count - ignored, 0)
    finally:
        sys.stdout , sys.stderr = oldio
