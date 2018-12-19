# -*- coding:utf-8 -*-
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import time
import telnetlib
import paramiko
time1=time.time()
ssh=paramiko.SSHClient()

##########登录目标服务器，下载文件到本地###############

def download_file_from_DNS(host,port,user,passwd,remote_path,local_path):
    t=paramiko.Transport((host,port))
    t.connect(username=user,password=passwd)
    sftp=paramiko.SFTPClient.from_transport(t)
    sftp.get(remote_path,local_path)
    t.close()


##########函数功能：能够提取ip地址，并且去重############

def read_file(input_file):
    fileop=open(input_file)
    pat='[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}'
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
    ids = list(set(iplist2))
    print "共解析ip个数:%s " % len(ids)
    return ids


def get_geolocation(ipaddr):
    rs=requests.get('https://freegeoip.net/json/'+ipaddr)
    info=[str(rs.json()['country_name']), str(rs.json()['city'])]
    return {'ip':ipaddr, 'country_name':info[0], 'city':info[1]}


def get_geolocation_list(ip_list):
    # location_list=[]
    location_value=[]
    for ip in ip_list:
        location=get_geolocation(ip)
        print "location_values is:",location.values()
        location_value.append(location.values())
        # location_list.append(location)
    return location_value


def output_file(output_file_name,location_value_list):
    out = open(output_file_name, "a")
    sep="\n"
    for each in location_value_list:
        # print each
        string = ""
        for i in xrange(len(each)):
            string=string+each[i]+","
        # string.strip()
        print "string is:",string
        out.write(string+sep)
    # 关闭连接
    out.close()


    ############主函数####################
if __name__ == "__main__":
    remote_path="/home/ben/dns/query.log.bak"
    local_path="C:/July_work/Files/dns_log.log"
    host_ip="47.104.171.204"
    port=22
    user_name="root"
    passwd="Qwer!@#$"
    output_file_name="C:/July_work/Files/myjob.csv"
    download_file_from_DNS(host_ip,port,user_name,passwd,remote_path,local_path)
    iplist=read_file(local_path)
    # # print(iplist2)
    location_value=get_geolocation_list(iplist)
    print "location_value is:",location_value
    output_file(output_file_name,location_value)

