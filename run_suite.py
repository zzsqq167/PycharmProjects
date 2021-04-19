import unittest
from script.login import login_code
from script.approvers import Aapprove
from script.trust import trust
import app,time
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(login_code))
suite.addTest(unittest.makeSuite(Aapprove))
suite.addTest(unittest.makeSuite(trust))

report_file=app.BASE_DIR+'/report/report{}.html'.format(time.strftime('%Y%m%d-%H%M%S'))

with open(report_file,'wb') as f:
    runner=HTMLTestRunner(f,title='金融项目p2p',description='测试金融项目')
    runner.run(suite)