# # -*- coding:UTF-8 -*-
# # 创建空元组
# tup1=()
# # 元组中只包含一个元素时，需要在元素后面添加逗号
# tup2=(50,)
# # 访问元组
# tup_1=('physics','chemistry',1997,2000)
# tup_2=(1,2,3,4,5,6,7)
#
# print "tup_1[0]: ",tup_1[0]
# print "tup_2[1:5]: ",tup_2[1:5]
#
# # 修改元组
# tup_3=(12,34,56)
# tup_4=('abc','xyz')
# # 以下修改元组元素操作是非法的
# # tup_3[0]=100
#
# # 创建一个新的元组
# tup_5=tup_3+tup_4
# print tup_5
# print tup_5 * 2
# print "length of tup_5 :",len(tup_5)
# if 12 in tup_5:
#     print "true"
# else:
#     print "flase"
#
# for x in tup_5:print x;
#
# # 删除元组
# print tup_1
# # del tup_1
# # print "after deleting tup_1 : "
# # print tup_1
#
# # 元组索引，截取
# L=('spam','Spam','SPAM!')
# print L[2]
# print(L[-2])
# print(L[1:])
#
# # 任意无符号的对象，以逗号隔开，默认为元组
# print 'abc',-4.24e93,18+6.6j,'xyz'
# x,y=1,2
# print "value of x , y : ",x,y
#
# # 元组内置函数
# # cmp(tuple1,tuple2)
# tuple1, tuple2=(123,'xyz'),(456,'abc')
# print cmp(tuple1,tuple2)
# print cmp(tuple2,tuple1)
# tuple3=tuple2+(786,)
# print cmp(tuple2,tuple3)
# tuple4=(123,'xyz')
# print cmp(tuple1,tuple4)
#
# # len(tuple)
# tuple_1,tuple_2=(123,'xyz','zara'),(456,'abc')
# print "first tuple length : ",len(tuple_1)
# print "second tuple length : ",len(tuple_2)
#
# # max(tuple)
# print "Max value element : ",max(tuple_1)
# print "Max value element : ",max(tuple_2)
#
# # min(tuple)
# print "Min value element : ",min(tuple_1)
# print "Min value element : ",min(tuple_2)
#
# # tuple(seq)
# list_1=[1,2,3,4,5]
# print "tuple(list): ",tuple(list_1)
# dict_1={1:2,3:4}
# print "tuple(dic): ",tuple(dict_1)
# print "tuple(tuple): ",tuple(tuple_1)
# aList=[123,'xyz','zara','abc']
# aTuple=tuple(aList)
# print "Tuple elements : ",aTuple