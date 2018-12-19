__author__='Administrator'
# -*- coding:utf-8 -*-
import functools
from ConfigParser import ConfigParser,NoSectionError
import os
cfg=ConfigParser()
config_file=os.path.dirname(os.path.abspath(__file__))+"\\testcaseconfig.conf"
print(config_file)
cfg.read(config_file)

def get_config(section,key):
    try:
        value=cfg.get(section,key)
    except:
        raise NoSectionError("config file %s has no section %s or no key %s"%(config_file,section,key))
    return value


if __name__=="__main__":
    print (get_config("user","user_ly"))
    print(get_config("ebackup","top"))
    print cfg.items("linux")
    print cfg.options("linux")
    print cfg.sections()
    for item in cfg.items("linux"):
        print(item)
