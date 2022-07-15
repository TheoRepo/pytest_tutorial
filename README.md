# Pytest开发测试代码
![2022最新pytest接口自动化测试框架](https://www.bilibili.com/video/BV1py4y1t7bJ?p=2&vd_source=8ba6ed28327bb7cef4adc064e3b342c1)

## 使用pytest, 默认的测试用例的规则以及基础应用
1. 模块名必须以test_或者_test结尾
2. 测试类必须以Test开头，并且不能有init方法
3. 测试方法必须以test开头

## pytest测试用例的运行方式

1. 主函数模型
    (1)运行所有: `pytest.main()`
    (2)运行模块: `pytest.main(['-vs', 'test_login.py'])`
    (3)指定目录: `pytest.main(['-vs', './interface_testcase'])`
    (4)指定nodeid: nodeid由模块名，分隔符，类名，方法名，函数名组成
        `pytest.main(['-vs','./interface_testcase/test_interface.py::test_04_func'])`
        `pytest.main(['-vs','./interface_testcase/test_interface.py::TestInterface::test_03_zhiliao'])`

2. 命令行模式
    (1)运行所有: `pytest`
    (2)运行模块: `pytest -vs test_login.py`
    (3)指定目录: `pytest -vs ./interface_testcase`
    (4)指定nodeid: `pytest -vs ./interface_testcase/test_interface.py::test_04_func`


参数详解:
-s : 表示输出调试信息，包括print打印的信息 
-v : 显示更详细的信息
-vs : 这两个参数一起用
-n : 支持多线程或者分布式运行
    如: `pytest -vs ./testcase/test_login.py -n 2`
--reruns NUM : 失败用例重跑
    如:`pytest.main(['-vs','./testcase', '--reruns=2'])`
    如:`pytest -vs ./testcase --reruns 2`
-x : 表示只要有一个用例出错，测试就停止
--maxfail : 出现两个用例失败就停止
-k : 根据测试用例的部分字符串指定测试用例
    如: `pytest -vs ./testcase -k "ao"`

3. 通过读取pytest.ini配置文件运行
pytest.ini单元测试框架的核心配置文件
    1. 位置: 一般是放在项目的根目录
    2. 编码: 必须是ANSI,可以使用notepad++修改编码格式
    3. 作用: 改变pytest默认的行为
    4. 运行的规则: 不管是主函数的模型运行，命令行模式运行，都会去读取这个配置文件

```text
[pytest]
addopts = -vs                   # 命令行参数， 用空格分隔
testpaths = ./testcase          # 测试用例的路径
python_files = test_*.py        # 模块名的规则
python_classes = Test*          # 类名的规则
python_functions = test         # 方法名的规则
```


## pytest 执行测试用例的顺序是怎样的呢？
pytest 默认从上到下
改变默认的执行顺序: 使用mark标记
`@pytest.mark.run(order=1)`

## 如何分组执行(冒烟，分模块执行，分接口和web执行)
我们可以指定某个一模块，某一个类，某个一个函数，某一个文件夹，去测试
那么我们可不可以指定不同的模块，分别测试其中一部分的用例

smoke: 冒烟用例，分布在各个模块里面

## 使用@pytest.fixture()装饰器来实现部分用例的前后置
`@pytest.fixture(scope="", params="", autouse="", ids="", name="")`
scope表示的是被@pytest.fixture标记的方法的作用域。function(默认), class, module, package/session

params : 参数化
autouse : 自动执行
ids : 当使用params参数化时给每一个值设置一个变量名
name : 表示被@pytest.fixture标记的方法，取一个别名