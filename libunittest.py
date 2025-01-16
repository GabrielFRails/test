import unittest

__testsuite = unittest.TestSuite()
def add_testcase_list(testcases):
# {
	global __testsuite

	alltests = list()
	for t in testcases:
		testlist = unittest.TestLoader().loadTestsFromTestCase(t)
		alltests.append(testlist)

	__testsuite.addTests(alltests)
# }


def run():
	return unittest.TextTestRunner(verbosity=3).run(__testsuite)
