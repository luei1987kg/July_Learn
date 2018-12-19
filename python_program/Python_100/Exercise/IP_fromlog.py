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
##########登录目标服务器###############
def telnetdo(host,user,passwd,command):
    if not host:
        try:
            host=sys.argv[1]
            user=sys.argv[2]
            passwd=sys.argv[3]
            command=sys.argv[4]
        except:
            print "Usage:telnetdo.py host user passed commend"
            return
    msg=['Debug messages:\n']
    tn=telnetlib.Telnet()
    try:
        tn.open(host)
    except:
        print "Cannot open host"
        return



def download_file_from_DNS(host,port,user,passwd,remote_path,local_path):
    t=paramiko.Transport((host,port))
    t.connect(username=user,password=passwd)
    sftp=paramiko.SFTPClient.from_transport(t)
    sftp.get(remote_path,local_path)
    t.close()


##########函数功能：能够提取ip地址，并且去重############
def read_file(input_file_name):
    _fLog=open(input_file_name)
    sep='\n'
    ip_list=[]
    for each in _fLog:
        print "each is:",each
        ip=re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',str(each),re.S)
        # print "ip is:",ip
        for i in ip:
            ip_list.append(i)
    #列表去重：通过set方法进行处理
    ids=list(set(ip_list))
    print "共解析ip个数:%s "%len(ids)
    _fLog.close()
    print "ip提取完毕***"
    return ids


def read_file2(input_file):
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


# 检查上次读的行数
def check(log_file,str_name):
    index=0
    with open(log_file,'r') as b:
        line=b.readline()
        while len(line)!=0:
            line=line.strip('\n')
            line=line.split('\t')
            if line[0].__eq__(str_name):
                index=int(line[1])
                b.close()
                break
            line=b.readline()
    return index


# 读文件之前看看上次的位置，以便继续读取。如果是第一次读取，那么记录到文件末尾的行数
def get(log_file,record_file):
    with open(log_file,'r') as f:
        index=check(log_file)#index=0代表是新加入的文件，所以文件指针索引为0，如果不是新加入的文件，为非0
        flag=False
        count=0
        if index != 0:
            line=f.readline()
            while len(line) != 0:
                count=count+1
                index=index-1
                if index == 0:
                    flag=True
                    break
                line=f.readline()
        if flag or index == 0:#flag=True,表明是从上次的位置继续开始读文件，或者这个文件是新加入的文件，
                            #我应该将文件指针读到文件末尾的位置和文件名保存到别一个文件中record_file
            line=f.readline()
            while len(line) != 0:
                count=count+1
                line=f.readline()
            with open(record_file,'w') as fil:
                fil_name_index=log_file+"\t"+str(count)
                fil.write(fil_name_index)


    ############主函数####################
if __name__ == "__main__":
    # remote_path="/home/ben/dns/query.log.bak"
    # local_path="C:/July_work/Files/dns_log.log"
    # host_ip="47.104.171.204"
    # port=22
    # user_name="root"
    # passwd="Qwer!@#$"
    # output_file_name="C:/July_work/Files/myjob.csv"
     input_file_name="C:/myjob.log"
     iplist=read_file(input_file_name)
     time2=time.time()
     print u'总共耗时：'+str(time2 - time1) + 's'
     print iplist
    # download_file_from_DNS(host_ip,port,user_name,passwd,remote_path,local_path)
    # iplist2=read_file2(local_path)
    # # # print(iplist2)
    # location_value=get_geolocation_list(iplist2)
    # print "location_value is:",location_value
    # output_file(output_file_name,location_value)