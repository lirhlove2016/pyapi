# coding=utf-8
import unittest
import time
from common import HTMLTestRunner
import os
from conf.conf import REPORTDIR

curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path): os.mkdir(report_path)
CASEDIR = os.path.join(curpath, "case")

def add_case(casepath=CASEDIR, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule,)
    return discover
def run_case(all_case,reportpath=REPORTDIR):
    '''执行所有的用例, 并把结果写入测试报告'''
    #取前面时间加入到测试报告文件名中
    now = time.strftime("%Y-%m-%d %M-%H_%M_%S", time.localtime(time.time()))           
    htmlreport = report_path+r"/"+now+"_result.html"
    print("测试报告生成地址：%s"% htmlreport)

    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)

    
    
