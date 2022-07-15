#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   test_mashang.py
#@Time    :   2022/07/14 15:44:39
#@Author  :   Theo Yu

import pytest

@pytest.fixture(scope="function", autouse=True)
def my_fixture():
    print('这是前后置的方法，可以实现部分以及全部用例的前后置')
    yield
    print('这是后置的方法')

class TestMashang:

    def test_01_baili(self):
        print('\n测试百里')

    def test_02_xingyao(self, my_fixture):
        print('\n测试星瑶')

# 预期
# test_01_baili没有前置
# test_02_xingyao有前置
