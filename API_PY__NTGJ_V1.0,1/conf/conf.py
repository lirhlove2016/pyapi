#!/usr/scripts/env python
# -*- coding: utf-8 -*-
import os
PROJECTPATH = r"D:\workdtation\mygitwork\pyapi\pyapi_dev_v1.0.0"

DATAFILE = os.path.join(PROJECTPATH, 'testdata\\bdh\\myapidata.xlsx')
curpath = os.path.dirname(os.path.realpath(__file__))
REPORTDIR = os.path.join(PROJECTPATH, 'report')
CASEDIR = os.path.join(PROJECTPATH, "case")
#DATADIR = os.path.join(SRCDIR, 'testdata')


if __name__ == "__main__":
    print(PROJECTPATH)
    print(DATAFILE)
    print(REPORTDIR)


    
