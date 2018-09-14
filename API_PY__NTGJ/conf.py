#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

#1
'''
testxlsx = r"D:\workdtation\debug\API_py_scripts_write\case\myapidata.xlsx"
newfile=r"D:\workdtation\debug\API_py_scripts_write\result\result.xls"
'''
#2
curpath=os.path.split(os.path.realpath(__file__))[0]
#testxlsx=curpath+"\\myapidata.xlsx"
testxlsx=curpath+"\\myapidata-all.xlsx"
newfile=curpath+"\\result.xls"                    
#print(curpath,testxlsx,newfile)

