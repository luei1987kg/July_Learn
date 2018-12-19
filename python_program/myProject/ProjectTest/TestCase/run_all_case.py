__author__='administrator'
# -*- coding:utf-8 -*-
import unittest
import os

case_path=os.path.join(os.getcwd())
print "case_path is:",case_path
report_path=os.path.abspath(os.path.dirname(__file__)+"\\"+os.path.pardir+r"\Result\ResultReport")
report_path1=os.path.abspath(os.getcwd()+"\\"+os.path.pardir+r"\Result\ResultReport")
print "report_path is:",report_path
print "report_path1 is:",report_path1

def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(all_case())