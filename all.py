#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   all.py
#@Time    :   2022/07/14 14:37:03
#@Author  :   Theo Yu


import pytest

if __name__ == '__main__':
    # pytest.main(['-vs','./interface_testcase']) # 运行目录
    # pytest.main(['-vs','./interface_testcase/test_interface.py::test_04_func']) # nodeid
    # pytest.main(['-vs','./testcase', '-n=2']) # 多线程
    # pytest.main(['-vs','./testcase', '--reruns=2']) # 失败重跑
    pytest.main()