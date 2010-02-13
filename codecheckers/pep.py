import pep8

class PyTestChecker(pep8.Checker):
    ignored_errors = 0
    def report_error(self, line_number, offset, text, check):
        if pep8.ignore_code(text[:4]): #XXX: pep8 is a retarded module!
            self.ignored_errors += 1
        pep8.Checker.report_error(self, line_number, offset, text, check)

def check_file(path):

    pep8.process_options(['pep8',
        #taken from moin
        '--ignore=E202,E221,E222,E241,E301,E302,E401,E501,E701,W391,W601,W602',
        '--show-source',
        'dummy file',
        ])
    checker = PyTestChecker(str(path))
    error_count = checker.check_all()
    ignored = checker.ignored_errors
    return max(error_count - ignored, 0)
