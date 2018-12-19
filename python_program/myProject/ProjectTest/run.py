__author__='Administrator'
import sys
import os
reload(sys)
modPath=os.path.dirname(__file__)+os.pardir
sys.path.append(os.path.abspath(modPath))

import time
from Libs.HTMLTestRunner import HTMLTestRunner
# from ProjectTest.LogKeyWords.logreport import *
from ProjectTest.TestCaseManagement.casemanagement import getAllTestCase,showAllTestCase,addTestCase

nametag=sys.argv[1]
now=time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())
reportPath=r".\Result\ResultReport"+"\\"
reportFile=reportPath+now+"_test_result.html"

def runSuite():
    allTestCase=getAllTestCase()
    testCaseChoice=showAllTestCase(allTestCase)
    suite=addTestCase(allTestCase,testCaseChoice)
    with open(reportFile,"wb") as fp:
        runner=HTMLTestRunner(stream=fp,title="report",description="testforHCP5.0",verbosity=2)
        x=runner.run(suite)
        print "x is:",x
        print "suite.countTestCases is:",suite.countTestCases()

if __name__=="__main__":
    runSuite()