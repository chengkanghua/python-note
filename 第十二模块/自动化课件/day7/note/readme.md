[toc]




# 内容回顾

1. 如何使用postman处理各式请求
    - get请求
    - post请求
    - 其他类型的请求
2. 在请求中如何携带参数
    - params
    - data, x-www-form-urlencoded    k:v    ---> content-type:application/x-www-form-urlencoded
    - json， raw， json ---> content-type:application/json
3. 特殊接口
    - cookies
        - 手动去浏览器做登录操作，获取cookies，然后，在postman发请求时，自己携带
        - 使用postman向登录接口发请求，如果该响应有cookies，就保存到cookies管理器中，当有想同域名的接口发送请求时，会去cookies管理器中，自动添加
    - token
        - 手动去浏览器做登录操作，获取token，然后，在postman发请求时，自己携带
        - 在postman中，首先向登录接口发请求，在请求结束后，手动的通过脚本获取token值，然后set到全局变量中；当向需要token的接口发请求时，在带上
    - 签名接口
        - 首先要知道该接口的加密算法   
        - 要手动的去处理各个参数和加密后的结果， set到环境变量中
        - 在请求的参数中使用`{{变量名}}`引用
    - webservice接口
        - 以xml格式作为数据交换的HTTP请求。 
        - 携带参数时，需要选择`xml`类型，注意，当你选择了`xml`类型，postman会自动的在请求头中携带content-type：application/xml
        - 但是，至于该接口的content-type需要什么值
    - 文件上传
        - 请求类型是 form-data
4. 环境管理
    - 自定义的环境变量，当使用时，直接选择即可
    - 全局的环境变量，可以定义基础的一些变量
    - 集合变量，作用域只作用于当前集合中
    - 内置的动态变量$guid
    - 使用，内置动态变量使用`{{$guid}}`, 其他引用直接`{{变量名}}`
5. 断言
    - 该功能就是在请求结束后要做的操作，不仅限于断言，还能，set变量，get变量，clear变量。
    - 断言：
        - 状态码断言，判断响应状态码是否是指定的状态码
        - 字符串断言，文本类型的请求结果中是否包含指定的字符
        - json断言，判断jsonData中，指定的key值是否符合预期
    - 在集合中，如果有一些公共的断言，可以写在集合的断言中，不用在每个接口里面写断言了，避免了重复造轮子，只需要在接口中实现接口特定的断言
6. 集合自动化
    - 能自动的将集合内的接口进行自动化运行，指定运行的轮次
    - 在自动化运行中，可以加入断言
    - 还可以做数据驱动测试，即测试数据来自外部的文件中，一般我们选择将外部数据保存为CSV和json类型。
        - CSV：是一个无格式的文本文件，但它可以使用Excel打开。
    - 可以导出json类型的运行结果。
7. 命令行测试
    - 在终端中进行执行postman脚本。
    - 要下载newman插件，该插件用来在终端中执行postman脚本，但该插件本身基于nodejs开发，所以要配置：
        - nodejs ---- 版本问题，不能太高，太高了，低版本的Windows报错，太低了，插件装不上，所以，选择 >=10版本的， 也不要选择最新版本的
        - nodejs有nmp(下载软件的工具)，在国内受网络影响，所以，配置cnpm，即淘宝的npm镜像
    - 在进行终端测试时，还需要导出html文件， 那就要在下载 reporter插件
    - 上述几个软件和插件下载完毕，可以执行命令：
        - newman run 脚本 -d 参数文件 -e 环境文件 -n 循环次数 -r html --reporter-html-export 测试报告路径

# unittest框架介绍

参考：https://www.cnblogs.com/Neeo/articles/11494077.html
unittest单元测试框架，它还能应用于web测试中。

unittest框架：
- 丰富断言类型
- 做数据驱动测试
- 自动化测试
- 测试报告

# unittest框架的下载
在python3中，unittest框架是python的内置模块，无需下载






# runTest

```python
import unittest
from case_set import CaseSet

class MyCase(unittest.TestCase):

    def runTest(self):
        if CaseSet().get_status_code() == 200:
            print('断言成功')
        else:

            print('断言失败')

if __name__ == '__main__':
    case = MyCase(methodName='aaa')
    case.run()
```
1. 类名可以自定义，但是必须继承unittest.TestCase
2. 当run的时候，会自动的找以methodName指定的方法名，然后执行它

# setUp/tearDown

```python
import unittest
import requests

class MyCase(unittest.TestCase):

    def setUp(self):
        self.code = requests.get("https://www.baidu.com").status_code
    #
    def tearDown(self):
        print("用例执行之后")

    def runTest(self):
        if self.code == 200:
            print('断言成功')
        else:
            print('断言失败')

if __name__ == '__main__':
    MyCase().run()
```
在用例执行执之前做的操作，写在`setUp`中；必须叫setUp， 做初始化的配置
在用例执行之后，要做的操作，在`tearDown`中实现，必须叫`tearDown`，用于收尾工作



# unittest断言和unittest.main

```python
import unittest
import requests

class MyCase(unittest.TestCase):

    def setUp(self):

        self.code = requests.get("https://www.baidu.com").status_code
        print("用力执行之前", self.code)
    def tearDown(self):
        print("用例执行之后")
        
    def test_case(self):
        self.assertEqual(self.code, 201, msg="实际值：{}   预期值 {}".format(self.code, 201))   # 实际值，预期值，错误描述

    def test_case_02(self):
        """ 第二个测试用例  """
        print(self._testMethodDoc, self._testMethodName)
        self.assertTrue(1)

if __name__ == '__main__':
    unittest.main()

```
用例执行成功用`.`表示，执行失败是`F`表示。
unittest.main()会自动的找到当前模块的unittest.TestCase的子类，然后找该子类内部以test开头的用例名，完事去一一的执行它们。

常用的断言：
- assertEqual(a, b, msg),  a == b ,否则断言失败
- assertNotEqual(a, b, msg),  a != b, 否则断言失败
- assertTrue(x, msg), 判断bool(x) == True, 否则断言失败
- assertFalse(x, msg), 判断bool(x) == False, 否则断言失败

如何输出用例名和用例描述信息(在用例中输出)：
- self._testMethodDoc，用例描述信息，即方法的注释内容
- self._testMethodName， 返回用例名


# unittest.TestSuite
TestSuite是测试套件，简单理解为承载多个用例的集合，或者把它想象成一个盒子，该盒子有多个用例。
当所有用例都添加到了盒子中，然后找一个执行器，去执行盒子中的测试用例。
我们要做的是：
- 实例化所有的用例
- 创建一个盒子
- 将用例添加到盒子中 
- 当所有用例都收集到盒子中后,使用执行器执行盒子中的测试用例

```python
import unittest

class MyCase(unittest.TestCase):

    def test_is_upper(self):
        self.assertTrue('Foo'.isupper())

    def test_is_lower(self):
        self.assertTrue('foo'.islower())


if __name__ == '__main__':
    # case_01 = MyCase(methodName='test_is_upper')
    # case_02 = MyCase(methodName='test_is_lower')

    case_obj = map(MyCase, ['test_is_upper', 'test_is_lower'])
    # print(case_obj, list(case_obj))
    # 创建suite
    suite = unittest.TestSuite()
    # 将用例添加到盒子中
    suite.addTests(case_obj)
    # 返suite中测试用例的个数
    # print(11111111, suite.countTestCases())

    # 使用执行器执行suite中的测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
```

在unittest.TestSuite中的方法：
- addTest，一个一个添加
- addTests,批量添加
- suite.countTestCases()，返回suite中用例个数

# unittest.makeSuite
unittest.makeSuite在实例化suite的时候，就同时做了收集用例的操作，直接返回一个收集用例完毕的suite；之后交给执行器去执行就玩腻了。


# unittest.TestLoader()

发现其他目录中的脚本用例：
- unittest.TestLoader().loadTestsFromModule，找到指定模块下面的TestCase的子类，获取其中以test开头的用例。
- unittest.TestLoader().loadTestsFromModule，获取指定模块中的，指定的用例
```python
import unittest
suite = unittest.TestLoader().loadTestsFromModule(ff_case)
    suite = unittest.TestLoader().loadTestsFromName(
        name="ff_case.TestCase.test_case_01",
        module=ff_case.TestCase
    )
    suite = unittest.TestLoader().loadTestsFromNames(
        names=[
            "ff_case.TestCase.test_case_01",
            "ff_case.TestCase.test_case_02",
        ],
        module=ff_case.TestCase
    )
```

- suite = unittest.TestLoader().discover(
        top_level_dir=index_dir,
        start_dir=SCRIPTS_DIR,
        pattern='ff_*'
    )
    - top_level_dir和start_dir的关系：
        - top_level_dir == start_dir,没问题
        - top_level_dir > start_dir, 没问题
        - top_level_dir < start_dir, 有问题

    - 注意，discover只会收集Python的包中以pattern开头的脚本，再找脚本中unittest.TestCase的子类中的以test开头的测试用例

# verbosity
verbosity用来控制用例输出的详细程度。
- verbosity=0， 精简模式。只输出执行错误的记录。
- verbosity=1, 默认模式，输出用例执行结果
- verbosity=2， 详细模式输出，用例来自于哪个模块下的哪个类中的哪个用例和它的执行结果。

# setupClass/tearDownClass

在用例前后执行的：
- setup/teardown
在所有的用例执行前后执行的：
- setUpClass/tearDownClass



# 跳过用例
有的情况下不需要某个用例执行，就用到了unittest.skip来完成：
- unittest.skip(reason)，跳过用例的描述
- unittest.skipif(condition, reason)   # 跳过的条件,跳过的原因

```python
import unittest


class MyCase(unittest.TestCase):


    def test_case_01(self):
        self.assertTrue(1)


    @unittest.skip(reason='无条件跳过')
    def test_case_02(self):
        self.assertTrue("")

    @unittest.skipIf(condition=3 < 2, reason='有条件跳过')
    def test_case_03(self):
        self.assertTrue(0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
```
在输出的窗口中，跳过的用例用`s`表示；断言成功`.`表示；断言失败`F`表示。

# 将结果输出到文件

```python
import unittest

class MyCase(unittest.TestCase):


    def test_case_01(self):
        self.assertTrue(1)


    # @unittest.skip(reason='无条件跳过')
    def test_case_02(self):
        self.assertTrue("")

    # @unittest.skipIf(condition=3 < 2, reason='有条件跳过')
    def test_case_03(self):
        self.assertTrue(0)


if __name__ == '__main__':
    suite = unittest.makeSuite(testCaseClass=MyCase, prefix='test')
    print(suite)

    f = open('a.txt', 'w')
    unittest.TextTestRunner(stream=f).run(suite)
```
主要使用stream参数，给个文件句柄即可。

# unittest生成测试报告
unittest搭配HTMLTestRunner模块来完成生成测试报告的操作。
unittest还可以跟BSTestRunner来生成测试报告。
**HTMLTestRunner下载**
该模块暂时没有在官网维护。只能私人搜索。
参考：https://www.cnblogs.com/Neeo/articles/7942613.html
将HTMLTestRunner.py/BSTestRunner.py放到python的第三方包中，`lib/site-packages/`

# 发送邮件

参考：https://www.cnblogs.com/Neeo/articles/11478853.html
参考：https://www.cnblogs.com/Neeo/articles/11199127.html#%E9%80%9A%E8%BF%87smtp%E5%8F%91%E9%82%AE%E4%BB%B6

1. 去QQ邮箱配置SMTP服务器和获取授权码
2. 编写测试用例
3. 生成测试报告
4. 使用第三方邮件服务发送测试报告





















































































