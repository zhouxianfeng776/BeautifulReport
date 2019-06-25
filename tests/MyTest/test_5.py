import unittest
import requests
import re

from MyTest.common.Cookie import GetCookie

url = "http://localhost:8070/"


class MyTestCase5(unittest.TestCase):


    def test_something(self):
        cookie=GetCookie.COOKIE
        if cookie:
            rp = requests.get(url + 'test/1111', cookies=cookie)
            print(rp.status_code)
        else:
            self.assertEqual(1,2)

if __name__ == '__main__':
    unittest.main()
