# -*- coding:utf-8 -*-
import math
import os

Money=2000
def AddMoney():
    global Money
    Money=Money+1
    print "globals parameter:",globals()
    print "local parameters:",locals()

# content=dir(math)
# print content
#
# print Money
AddMoney()
# print Money

# str=raw_input("please input:")
# print "the content of raw_input is:",str
#
# str2=input("please input again:")
# print "the content of input is:",str2

fo=open("foo.txt","w")
print "file name:",fo.name
print "file is close or not:",fo.closed
print "file open mode:",fo.mode
print "file end is force add space or not:",fo.softspace
fo.write("www.runoob.com!\nVery good site!\n")
fo.close()

# 打开一个文件
fo=open("foo.txt","r+")
str=fo.read(10)
print "read string is:",str

# 查找当前位置
position=fo.tell()
print "local position is:",position

# 把指针再次重新定位到文件开头
position=fo.seek(0,0)
str=fo.read(10)
print "re-read string is:",str

# 关闭打开的文件
fo.close()

fo=open("test1.txt","w")
fo.write("this is a test")
fo.close()
os.rename("test1.txt","test2.txt")
fo=open("test2.txt","r+")
fo.write("overwrite")
fo.close()
os.remove("test2.txt")

# os.mkdir("test_test")
print "local dirctory:",os.getcwd()
os.chdir(r"D:\JULY\python_program\Python_100\Exercise\test_test")
# os.rmdir("test_test")

