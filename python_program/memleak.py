#coding=utf-8
#此脚本用于监控linux某个进程的CPU，内存占用情况
import os,time,sys
print "使用方法 python memleak.py 进程名 监控时间间隔"
processname=sys.argv[1]
sleeptime=sys.argv[2]
filename=processname+time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+".log"
processname_pid="pgrep -l -f "+processname+" | grep -w"+processname+" |grep -v grep|grep -v python | awk`{print $1}`"
pid_output=os.popen(processname_pid)
print "Process: "+processname, "PID: "+pid_output.read()
#processname_pid="$("+processname_pid+")"
title="echo \"Date Time PID RSS(物理内存-KB) VSZ(虚拟内存-KB) %CPU %Mem\">>"+filename
os.system(title)
cmdpara="echo $(data \"+%Y-%m-%d %H:%M:%S\") $(ps -e -o `pid,rss,vsz,%cpu,%mem,command` | grep -v grep | grep -v python | grep -w"+processname+" | awk `{print $1,$2,$3,$4,$5}`) >>"+filename
#print cmdpara
while 1:
    os.system(cmdpara)
    time.sleep(int(sleeptime))

