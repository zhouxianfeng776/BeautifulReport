import unittest
import requests
import re


url = "http://localhost:8070/"
cookie = None

class MyTestCase3(unittest.TestCase):

    def test_get_session(self):
        global cookie
        t = requests.get(url + "login")
        p = '<input name="_csrf" type="hidden" value="([\da-z-]+)" />'
        matchObj = re.search(p, t.text)
        if matchObj:
            csrf = matchObj.group(1)
            payload = {'username': '1', 'password': '1', '_csrf': csrf}
            resp = requests.post(url + "login", data=payload, cookies=t.cookies,allow_redirects=False)
            cookie=resp.cookies
            # print(resp.status_code)
            self.assertEqual(resp.status_code,302)
            print('登录成功：',cookie)

    def test_something(self):
        if cookie:
            rp = requests.get(url + 'test/1111', cookies=cookie)
            print(rp.content)

    def test_something1(self):
        if cookie:
            rp = requests.get(url + 'test/2222', cookies=cookie)
            print(rp.content)

    def test_something2(self):
        if cookie:
            rp = requests.get(url + 'test/333', cookies=cookie)
            print(rp.content)

    def test_z_logout(self):
        if cookie:
            t = requests.get(url + "logout",cookies=cookie)
            p = '<input name="_csrf" type="hidden" value="([\da-z-]+)" />'
            matchObj = re.search(p, t.text)
            if matchObj:
                csrf = matchObj.group(1)
                payload = { '_csrf': csrf}
                print(payload)
                resp = requests.post(url + "logout", data=payload, cookies=cookie, allow_redirects=False)
                print(resp.status_code)
                print('登出成功：', cookie)

    def test_something3(self):
        if cookie:
            rp = requests.get(url + 'test/333', cookies=cookie)
            print(rp.content)

if __name__ == '__main__':
    unittest.main()
