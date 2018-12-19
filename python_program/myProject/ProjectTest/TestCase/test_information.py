__author__='administrator'
# -*- coding:utf-8 -*-
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print "start!"
    def tearDown(self):
        time.sleep(1)
        print"end!"
    def test01(self):
        print"执行测试用例01"

    def test03(self):
        print"执行测试用例03"

    def test02(self):
        print "执行测试用例02"

# if __name__=="__main__":
#     unittest.main()
#     tester=Test()
#     tester.setUp()
#     tester.test01()
#     tester.test02()
#     tester.test03()
#     tester.tearDown()