#!/usr/bin/python
# -*- encoding: utf-8 -*-
#@File    :   test_product.py
#@Time    :   2022/07/14 14:35:26
#@Author  :   Theo Yu

import time
import pytest

class TestProduct:

    
    def test_02_xingyao(self):
        time.sleep(3)
        print('测试星瑶')

if __name__ == '__main__':
    pytest.main(['-s'])