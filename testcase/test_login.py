#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   test_login.py
#@Time    :   2022/07/14 14:18:59
#@Author  :   Theo Yu

import time
import pytest

class TestLogin:

    def test_01_baili(self):
        print('测试百里')

    @pytest.mark.run(order=2)
    def test_02_xingyao(self):
        print('测试星瑶')

    @pytest.mark.run(order=1)
    def test_03_zhiliao(self):
        print('测试知了')
        assert 1==2

    @pytest.mark.run(order=3)
    def test_04_weiwei(self):
        print('测试微微')

    def test_05_huahua(self):
        print('测试花花')


if __name__ == '__main__':
    pytest.main()