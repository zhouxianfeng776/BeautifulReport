import os
import time
import unittest
from BeautifulReport import BeautifulReport

if __name__ == "__main__":
    # 定义测试报告的生成的时间，时间戳
    nowTime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    # test_dir"目录，"test*.py"匹配当前目录下所有test*.py结尾的用例
    test_dir = os.path.abspath(os.path.join(os.getcwd(), "../"))
    suite_tests = \
        unittest.defaultTestLoader.discover(test_dir, pattern="test*.py",
                                            top_level_dir=None)
    BeautifulReport(suite_tests).report(filename='ApiReport' + '_' + nowTime,
                                        description='中台接口测试',
                                        log_path='./')




# /***
#  *                    _ooOoo_
#  *                   o8888888o
#  *                   88" . "88
#  *                   (| -_- |)
#  *                    O\ = /O
#  *                ____/`---'\____
#  *              .   ' \\| |// `.
#  *               / \\||| : |||// \
#  *             / _||||| -:- |||||- \
#  *               | | \\\ - /// | |
#  *             | \_| ''\---/'' | |
#  *              \ .-\__ `-` ___/-. /
#  *           ___`. .' /--.--\ `. . __
#  *        ."" '< `.___\_<|>_/___.' >'"".
#  *       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#  *         \ \ `-. \_ __\ /__ _/ .-` / /
#  * ======`-.____`-.___\_____/___.-`____.-'======
#  *                    `=---='
#  *
#  * .............................................
#  *          佛祖保佑             永无BUG
#  */