__author__='Administrator'
# -*- coding:utf-8 -*-
from ProjectTest.LogKeyWords.logreport import *
from ProjectTest.Config.configprase import get_config
import os
import sys
import unittest

currPath=os.path.dirname(__file__)
currPath1=os.getcwd()
print("________________")
print"currPath is:",currPath
print "currPath1 i:",currPath1
testCasePath=os.path.abspath(currPath1+"\\"+os.path.pardir+r"\TestCase")
print("***************")
print("os.path.pardir is:",os.path.pardir)
print("#########################")
print("testCasePath is:",testCasePath)
testMoudlePath=get_config("testcase","tcMPath")
print("++++++++++++++++++++")
print("testMoudlePath is:",testMoudlePath)

def getAllTestCase(path=testCasePath):
    print "testcase path is:",testCasePath
    suite=unittest.defaultTestLoader.discover(path,pattern="test*.py")
    print"suite is:",suite
    testCaseCount=suite.countTestCases()
    print"testcase count is:",testCaseCount
    print"str(suite) is:",str(suite)
    suite_list_tmp=str(suite).split("tests=")[-testCaseCount:]
    print "suite_list_tmp is:",suite_list_tmp
    tmp_list=[]
    for i in suite_list_tmp:
        for j in i.split(","):
            if "testMethod" in j:
                tmp_list.append(j)
    print"tmp_list is:",tmp_list
    result_list=[]
    for item in tmp_list:
        no=tmp_list.index(item)
        result_dict={}
        tmp01=item.split()
        for x in tmp01:
            s=x.replace("[","").replace("<","").replace("]","").replace(">","")
            result_dict["No"]=no
            print"s is:",s
            if "." in s:
                result_dict["fileName"]=s.split(".")[0]
                result_dict["className"]=s.split(".")[1]
            else:
                result_dict["testCase"]=s.split("=")[-1]
        result_list.append(result_dict)
    print"all testcases are:",result_list
    return result_list


def showAllTestCase(testcaselist):
    # print args
    no="No"
    fileName="fileName"
    className="className"
    testCase="testCase"
    print "All Testcases as below,please choose (A stand for all test cases):"
    result=[]
    print " no: testcase"
    for index,value in enumerate(testcaselist):
        if (index)%20==0:
            print "%4s:%15s:%15s:%15s"%(no,fileName,className,testCase)
        print "%4s:%15s:%15s:%15s"%(value[no],value[fileName],value[className],value[testCase])
        if (index%20==19 and index!=0) or index == len(testcaselist)-1:
            print "the %d page shows complete. total %d pages please input your choice, n for next page,\
             q for quit,\n number for the test case you choose, 1C for the class you choose, 1F for \
             the file you choose:"%(index/20,len(testcaselist)/20+1)
        input_tmp=raw_input()
        if input_tmp in ["q","Q"]:
            break
        elif input_tmp in ["a","A"]:
            print "you choosed all test cases.please input another choices:"
            result.append(input_tmp)
            break
        else:
            while True:
                if input_tmp in ["n","N"]:
                    break
                elif input_tmp.isdigit():
                    result.append(int(input_tmp))
                elif input_tmp in ["q","Q"]:
                    break
                elif input_tmp[-1] in ["c","C","f","F"]:
                    result.append(input_tmp)
                elif input_tmp in ["a","A"]:
                    print "you choose all test cases. please input another choice:"
                    result.append(input_tmp)
                    break
                else:
                    print "%s is a wrong input. please re-input"%input_tmp
                    input_tmp=raw_input()
            if input_tmp in ["q","Q"]:
                break
    print "all choice is:",result
    return result


def importModule(modulePath,fromlist=[]):
    try:
        mod=__import__(modulePath,formlist=fromlist)
    except:
        print "import module %s error"%testMoudlePath+"."+fromlist[0]
        raise ImportError("import module %s error"%(testMoudlePath+"."+fromlist[0]))
    return mod


def addTestCase(testCases,choice):
    if choice == ["a"] or choice == ["A"]:
        suite=unittest.defaultTestLoader.discover(testCasePath,pattern="test*.py")
    elif choice != []:
        suite=unittest.TestSuite()
        for index,value in enumerate(choice):
            if isinstance(value,int):
                fileName=testCases[value]["fileName"]
                testClass=testCases[value]["className"]
                testModPath=testCases[value]["testCase"]
                mod=importModule(testModPath,fromlist=[testClass])
                className=getattr(mod,testClass)
                suite.addTest(className(testClass))
            elif value[-1] in ["c","C"]:
                suite_tmp=unittest.TestLoader()
                value_index=int(value[0])
                fileName=testCases[value_index]["fileName"]
                testClass=testCases[value_index]["className"]
                testModPath=testMoudlePath+"."+fileName
                mod=importModule(testModPath,fromlist=[testClass])
                print "mod is:",mod
                className=getattr(mod,testClass)
                print "className is:",className
                suite_tmp=unittest.TestLoader().loadTestsFromTestCase(className)
                print "suite_tmp is:",suite_tmp
                suite.addTests(suite_tmp)
            else:
                print "no choice input, error"
                raise IndexError("no choice input, error")
    print "suite is:",suite
    return suite

if __name__=="__main__":
   allTestCase=getAllTestCase()
   testCaseChoice=showAllTestCase(allTestCase)
   addTestCase(allTestCase,testCaseChoice)