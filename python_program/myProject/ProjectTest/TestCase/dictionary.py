# # -*- coding:UTF-8 -*-
# # 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中
# # 键必须是唯一的，但值则不必
# # 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
# # 一个简单的字典实例：
# dict1={'Alice':'2341','Beth':'9102','Cecil':'3258'}
# dict2={'Name':'Zara','Age':7,'Class':'First'}
# # 访问字典里的值
# print "dict1['Alice']: ",dict1['Alice']
# print "dict1['Beth']: ",dict1['Beth']
# # 如果用字典里没有的键访问数据，会输出错误
# # print "dict1['Name']: ",dict1['Name']
#
# # 修改字典
# # 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
# dict2['Age']=8
# dict2['School']="DPS School"
# print "dict2['Age']: ",dict2['Age']
# print "dict2['School']: ",dict2['School']
#
# # 删除字典元素
# # 能删单一的元素也能清空字典，清空只需一项操作
# del dict2['Name']  # 删除键是'Name'的条目
# dict2.clear()  # 清空词典所有条目
# del dict2 # 删除词典
#
# # print "dict2['Age']: ", dict2['Age']
# # print "dict2['School']: ", dict2['School']
#
# # 字典键的特性
# # 字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# # 两个重要的点需要记住：
# # 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下：
# dict3 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
# print "dict3['Name']: ",dict3['Name']
# # 2)键必须不可改变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下：
# # dict5={['Name']: 'Zara', 'Age': 7}
# # print "dict5['Name']: ",dict5['Name']
#
# # 字典内置函数&方法
# # cmp(dict1, dict2),比较两个字典元素,
# # 如果两个字典的元素相同返回0，如果字典dict1大于字典dict2返回1，如果字典dict1小于字典dict2返回-1
# dict_1 = {'Name': 'Zara', 'Age': 7}
# dict_2 = {'Name': 'Mahnaz', 'Age': 27}
# dict_3 = {'Name': 'Abid', 'Age': 27}
# dict_4 = {'Name': 'Zara', 'Age': 7}
# print "Return value : %d"% cmp(dict_1,dict_2)
# print "Return value : %d"%cmp(dict_2,dict_3)
# print "Return value : %d"%cmp(dict_1,dict_4)
#
# # len(dict),计算字典元素个数，即键的总数
# # 返回字典的元素个数
# print "Length : %d" % len (dict_1)
#
# # str(dict),输出字典可打印的字符串表示
# # 返回字符串
# print "Equivalent string : %s"%str(dict_1)
#
# # type(variable),返回输入的变量类型，如果变量是字典就返回字典类型
# # 返回输入的变量类型
# print "Variable type : %s"%type(dict_1)
#
# # dict.clear(),删除字典内所有元素
# # 该函数没有任何返回值
# print "Start Len : %d"%len(dict_1)
# dict_1.clear()
# print "End Len : %d"%len(dict_1)
#
# # dict.copy(),返回一个字典的浅复制
# dict_5=dict_2.copy()
# print "New dictionary : %s"%str(dict_5)
#
# # 直接赋值和 copy 的区别
# dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
# dict2 = dict1  # 浅拷贝: 引用对象
# dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# # 修改 data 数据
# dict1['user'] = 'root'
# dict1['num'].remove(1)
# # 输出结果
# print(dict1)
# print(dict2)
# print(dict3)
#
# # dict.fromkeys(seq[,val])，创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# seq=('name','age','sex')
# dicts=dict.fromkeys(seq)
# print "new dictionary : %s"%str(dicts)
# dicts2=dict.fromkeys(seq,10)
# print "New Dictionary : %s"%str(dicts2)
#
# # dict.get(key,default=None)，返回指定键的值，如果值不在字典中返回default值
# dict2={'Name':'Zara','Age':27}
# print "Value : %s"%dict2.get('Age')
# print "Value : %s"%dict2.get('Sex',"Never")
#
# # dict.has_key(key)，如果键在字典dict里返回true，否则返回false
# print "Vaule : %s"%dict2.has_key('Age')
# print "value : %s"%dict2.has_key('Name')
# print "value : %s"%dict2.has_key('Sex')
#
# # dict.items()，以列表返回可遍历的（键，值）元组数组
# dict1={'Google':'www.google.com','Runoob':'www.runoob.com','taobao':'www.taobao.com'}
# print "字典值 ： %s"%dict1.items()
# for key,value in dict1.items():
#     print key,value
#
# # dict.keys()，以列表返回一个字典所有的键
# print "value : %s"%dict2.keys()
# print "value : %s"%dict1.keys()
#
# # dict.setdefault(key,default=None)，和get()类似，但如果键不存在于字典中，将会添加键并将值设为default
# dict1={'runoob':'菜鸟教程','google':'Google搜索'}
# print "value : %s"%dict1.setdefault('runoob',None)
# print "value : %s"%dict1.setdefault('taobao','淘宝')
# print "value : %s"%dict1
#
# # dict.update(dict2)，把字典dict2的键/值对更新到dict里
# dict1={'Name':'Zara','Age':7}
# dict2={'Sex':'female'}
# dict1.update(dict2)
# print "value : %s"%dict1
#
# # dict.values()，以列表返回字典中的所有值
# print "value : %s"%dict1.values()
#
# # pop(key[,default])，删除字典给定键key所对应的值，返回值为被删除的值。key值必须给出。否则，返回default值
# site={'name':'菜鸟教程','alexa':10000,'url':'www.runoob.com'}
# pop_obj=site.pop('name')
# print pop_obj
# print site
#
# # popitem(),随机返回并删除字典中的一对键和值
# site={'name':'菜鸟教程','alexa':10000,'url':'www.runoob.com'}
# pop_obj=site.popitem()
# print(pop_obj)
# print(site)