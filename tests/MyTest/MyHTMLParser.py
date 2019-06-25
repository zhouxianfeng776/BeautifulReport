from HTMLParser import HTMLParser

class MyHtmlParese(HTMLParser):
    def test_null(self):
        print()


if __name__ == '__main__':
    parese=MyHtmlParese()
    parese.feed("")