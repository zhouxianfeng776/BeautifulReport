import unittest


class MyTestCase1(unittest.TestCase):

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print(22222)

    def test_something1(self):
        print("test111111")
        self.assertEqual(True, True,"test111")

    def test_something2(self):
        print("test12222")
        self.assertEqual(True, True,"test111")
    def test_something3(self):
        print("test13333")
        self.assertEqual(True, True,"test111")

    def test_something4(self):
        print("test14444444")
        self.assertEqual(True, True,"test111")


if __name__ == '__main__':
    unittest.main()
