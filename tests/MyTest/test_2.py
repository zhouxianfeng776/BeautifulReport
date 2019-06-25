import unittest

import os
import requests
from common.readExcel import ReadExcel

import re

url = "http://localhost:8070/"

cookie = ''


class MyTestCase2(unittest.TestCase):
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print(22222)

    def test_something1(self):
        a = ['a', 'b', 'c']
        b = [1, 2, 3]

        dt = dict(zip(b, a))
        print(dt)
        print(dt[1])
        print(dt)

        for x in zip(a, b):
            print(x)

    def test_something2(self):
        t = ReadExcel()
        data = t.readExcel('C:\\Users\\01384526\\PycharmProjects\\RequestsApi\\Data\\ExcelData\\TestCase.xlsx')
        print(data)

    def test_requests(self):
        t = requests.get(url + "login")
        print(t.url)
        # print(t.content)
        print(t.headers)
        # print(t.text)
        print(t.status_code)
        print(t.cookies)
        # dict(Cookie=t.headers.get('Set-Cookie'))
        p = '<input name="_csrf" type="hidden" value="([\da-z-]+)" />'
        matchObj = re.search(p, t.text)
        if matchObj:
            print(matchObj.group(1))
            csrf = matchObj.group(1)
            payload = {'username': '1', 'password': '1', '_csrf': csrf}
            resp = requests.post(url + "login", data=payload, cookies=t.cookies,allow_redirects=False)
            print(resp.content)
            print(resp.history)
            print(resp.status_code)
            print(resp.headers)
            print(resp.cookies)
            cookie=resp.cookies
            rp=requests.get(url+'test/1111',cookies=cookie)
            print(rp.content)

    def test_re(self):
        # pattern='[^abc]'
        # str='plain'
        # tag1=re.findall('plain',pattern)
        # print(re.match(pattern, str))
        # print( re.match(pattern,str).span())
        # print(re.match('ww', 'wwww.runoob.com').span())  # 在起始位置匹配
        # print(re.match('com', 'wwww.runoob.com'))

        # line = "Cats are smarter than dogs"
        # matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
        line = '111<input name="_csrf" type="hidden" value="7f94933d-744c-4bee-90a1-21b938e5f2f1" />'
        p = '<input name="_csrf" type="hidden" value="([\da-z-]+)" />'
        matchObj = re.search(p, line)

        if matchObj:
            print("matchObj.group() : ", matchObj.group())
            print("matchObj.group(1) : ", matchObj.group(1))
            # print("matchObj.group(2) : ", matchObj.group(2))
        else:
            print("No match!!")

        str = '<button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>'
        p = '^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$'

        # if tag1:
        #     print("11")
        #     print(tag1)


if __name__ == '__main__':
    unittest.main()
