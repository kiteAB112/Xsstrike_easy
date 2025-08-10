#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import imp
import parser
import sys
# check python version and exit if not python3
if sys.version_info[0] < 3:
    print("Python 2 is not supported. Please use Python 3.4 or higher.")
    exit()

# check package fuzzywuzzy and install if not installed
try:
    import fuzzywuzzy
except ImportError:
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "pip3", "install", "fuzzywuzzy"])
        print("fuzzywuzzy installed successfully. Please restart the program.")
        exit()
    except subprocess.CalledProcessError as e:
        print("Installation failed: Command execution error")
        raise ImportError("Unable to install the fuzzywuzzy library. Please install it manually.")

# import whatever we need from standard library
import json
import argparse

# and configurations core Lib
import core.log
import core.config

# Processing command line arguments, where dest var names will be mapped to local vars with the same name

parser = argparse.ArgumentParser(description="Xsstrike - A powerful XSS scanner")
parser.add_argument("-u", "--url", help="Target URL to scan",dest='target')
parser.add_argument('--data',help='POST data',dest='paramData')
parser.add_argument('--proxy',help='Proxy to use for requests',dest='proxy',action='store_true') # maybe change this in config is better,consider the commandline may be too cluttered

parser.add_argument('--console-log-level',help='Log level for console output',dest='console_log_level',default='core.log.console_log_level')
parser.add_argument('--log-file',help='Log file to use for output',dest='log_file',default='core.log.log_file')
parser.add_argument('--file-log-level',help='Log level for file output',dest='file_log_level',default='core.log.file_log_level')




# pull all parameter values of dict from argparse namespace into Local variables of name == key

args = parser.parse_args()
target = args.target
paramData = args.paramData
proxy = args.proxy

core.log.console_log_level = args.console_log_level
core.log.log_file = args.log_file
core.log.file_log_level = args.file_log_level

logger = core.log.setup_logger()

core.config.globalVariables = vars(args) # store args in globalVariables,for use in other modules


if not proxy:
    core.config.proxy = None

# 这里只是简单的两种，一个是有 --data，一个是没有 --data

scan(target,paramData)






