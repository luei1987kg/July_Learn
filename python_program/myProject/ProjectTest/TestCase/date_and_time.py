# # -*- coding:UTF-8 -*-
#
# # python提供了一个time和calendar模块可以用于格式化日期和时间。
# # 时间间隔是以秒为单位的浮点小数
# # 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示
# # python的time模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳
#
# import time
#
# ticks=time.time()
# print "当前时间戳为: ",ticks
#
# # 时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年
#
# # 什么是时间元组,struct_time
# # 获取当前时间
# # 从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数
# localtime=time.localtime(time.time())
# localtime=time.localtime()
# print "本地时间为: ",localtime
#
# # 获取格式化的时间
# # 你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime()
# localtime=time.asctime(time.localtime(time.time()))
# localtime=time.asctime()
# print "本地时间为: ",localtime
#
# # 格式化日期，我们可以使用time模块的strftime方法来格式化日期
# # 格式化成2016-03-20 11:45:39形式
# print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
# # 将格式字符串转换为时间戳
# a="Sat Mar 28 22:24:24 2016"
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
#
# import calendar
#
# cal=calendar.month(2017,1)
# print "以下输出2017年1月份的日历："
# print cal