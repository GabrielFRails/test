# test
wrapper around unittest python module

## usage
Create your tests and put then on a list

```
class MyTestCase(unittest.TestCase):
	...

testcase_list = [MyTestCase]
```

import the lib and the test cases lists
```
# import libunittest as ut

# from mytestcase import testcase_list

ut.add_testcase_list(testcase_list)
ut.run()
```