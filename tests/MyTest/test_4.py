import unittest
import requests
import re

from MyTest.common.Cookie import GetCookie

url = "http://localhost:8070/"


class MyTestCase4(unittest.TestCase):

    def test_get_session(self):
        t = requests.get(url + "login")
        p = '<input name="_csrf" type="hidden" value="([\da-z-]+)" />'
        matchObj = re.search(p, t.text)
        if matchObj:
            csrf = matchObj.group(1)
            payload = {'username': '1', 'password': '1', '_csrf': csrf}
            resp = requests.post(url + "login", data=payload, cookies=t.cookies,allow_redirects=False)
            # print(resp.status_code)
            self.assertEqual(resp.status_code,302)
            GetCookie.COOKIE=resp.cookies

    def test_something(self):
        cookie=GetCookie.COOKIE
        if cookie:
            rp = requests.get(url + 'test/1111', cookies=cookie)
            print(rp.content)

if __name__ == '__main__':
    unittest.main()
