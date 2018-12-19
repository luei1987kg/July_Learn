# -*- coding:utf-8 -*-
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import time
import urllib2
# urllib2.path.append('C:/Python27/Lib/socket.py')
time1=time.time()

##########登录目标服务器###############

##########函数功能：能够提取ip地址，并且去重############
def read_file(input_file_name):
    _fLog=open(input_file_name)
    sep='\n'
    ip_list=[]
    for each in _fLog:
        print "each is:",each
        ip=re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',str(each),re.S)
        ip_list.append(ip[0])
    #列表去重：通过set方法进行处理
    ids=list(set(ip_list))
    print "共解析ip个数:%s "%len(ids)
    ##写出数据到本地
    #设置输出文件路径
    # out=open(output_file_name,"a")
    # # out.write("ip"+sep)
    # for each in ids:
    #     print each
    #     out.write(each+sep)
    # # 关闭连接
    # out.close()
    _fLog.close()
    print "ip提取完毕***"
    return ids

def get_iplocation(ipaddr):
    try:
        while True:
            url = "http://www.ip138.com/ips138.asp?ip=%s&action=2" % ipaddr
            print "url is:",url
            u=urllib2.urlopen(url)
            s=u.read()
            print "s is:",s
            result=re.findall(r'(<li>.*?</li>)',s)
            for i in result:
                print i[4:-5]
            print "*"*45
            print "\n"
    except:
        print "Not Data Find"

def lookup(ipaddr):
    URL='http://freeipapi.17mon.cn/'+ipaddr
    try:
        res=requests.get(URL,timeout=3)
    except requests.RequestException as e:
        print(e)

    json_data=res.json()
    print "所在国家："+json_data[0].encode('utf-8')
    print "所在省份："+json_data[1].encode('utf-8')
    print "所在城市："+json_data[2].encode('utf-8')
    return ipaddr

def get_geolocation(ipaddr):
    rs=requests.get('https://freegeoip.net/json/'+ipaddr)
    info=[str(rs.json()['country_name']), str(rs.json()['city'])]
    return {'ip':ipaddr, 'country_name':info[0], 'city':info[1]}

def read_file2(input_file):
    fileop=open(input_file)
    pat='[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}'
    # ipcount={}
    iplist2=[]
    while True:
        # 每次从文件中读取一行
        item=fileop.readline()
        # 判断是否已经到达文件末尾
        if item:
            itemip=re.findall(pat,item)
            for ip in itemip:
                iplist2.append(ip)
        else:
            print "文件读取完毕\n"
            fileop.close()
            break
    list = list(set(iplist2))
    print "共解析ip个数:%s " % len(list)
    return list

    ############主函数####################
if __name__ == "__main__":
    input_file_name="C:/myjob.log"
    # output_file_name="C:/myjob.txt"
    iplist=read_file(input_file_name)
    time2=time.time()
    print u'总共耗时：'+str(time2 - time1) + 's'
    print iplist
    iplist2=read_file2(input_file_name)
    print(iplist2)
    # for ipaddr in iplist:
    #      print(get_geolocation(ipaddr))