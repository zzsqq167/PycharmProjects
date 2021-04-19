import unittest
import requests
import logging
from utils import assertEqual_utils
from api.approveAPI import approveApi
from api.logAPI import logAPI

class Aapprove(unittest.TestCase):
    def setUp(self) ->None:
        self.session=requests.Session()
        self.approveApi=approveApi()
        self.logAPI=logAPI()
        #可登录号码
        self.phone='13798987192'
        #可登录号码，未认证
        self.phone1='13798987199'
        self.password='test123'

    def tearDown(self):
        self.session.close()


    def test01_approve(self):
        reponse=self.logAPI.loginenroll(self.session,self.phone,self.password)
        assertEqual_utils(self,reponse,200,200,'登录成功')
        reponse = self.approveApi.approve(self.session,'向玉宇','41080119930228457X')
        logging.info('log={}'.format(reponse.json()))
        self.assertEqual(200,reponse.status_code)
        self.assertEqual(200,reponse.json().get('status'))
        #self.aeerstEqual({"card_id":"110****21X","realname":"李**"},reponse.josn().get('data'))
        self.assertEqual('提交成功!',reponse.json().get('description'))

    def test02_approve_name_null(self):
        reponse=self.logAPI.loginenroll(self.session,self.phone1,self.password)
        assertEqual_utils(self,reponse,200,200,'登录成功')
        reponse = self.approveApi.approve(self.session,'','130683199011300601')
        logging.info('log={}'.format(reponse.json()))
        assertEqual_utils(self,reponse,200,100,'姓名不能为空')

    def test03_approve_id_null(self):
        reponse=self.logAPI.loginenroll(self.session,self.phone1,self.password)
        assertEqual_utils(self,reponse,200,200,'登录成功')
        reponse = self.approveApi.approve(self.session,'喀喀喀','')
        logging.info('log={}'.format(reponse.json()))
        assertEqual_utils(self,reponse,200,100,'身份证号不能为空')

    def test04_approve_id_exists(self):
        reponse=self.logAPI.loginenroll(self.session,self.phone1,self.password)
        assertEqual_utils(self,reponse,200,200,'登录成功')
        reponse = self.approveApi.approve(self.session,'向玉宇','41080119930228457X')
        logging.info('log={}'.format(reponse.json()))
        assertEqual_utils(self,reponse,200,100,'身份证号已存在')

    def test05_approve_id_format_wrong(self):
        reponse=self.logAPI.loginenroll(self.session,self.phone1,self.password)
        assertEqual_utils(self,reponse,200,200,'登录成功')
        reponse = self.approveApi.approve(self.session,'向玉宇','410801')
        logging.info('log={}'.format(reponse.json()))
        assertEqual_utils(self,reponse,200,100,'身份证号格式不正确')

    def test06_approve_query(self):
        reponse=self.logAPI.loginenroll(self.session,self.phone,self.password)
        assertEqual_utils(self,reponse,200,200,'登录成功')
        reponse=self.approveApi.approvequery(self.session)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual('-1',reponse.json().get('is_email_open'))

    def test07_approve_query(self):
        reponse=self.logAPI.loginenroll(self.session,self.phone1,self.password)
        assertEqual_utils(self,reponse,200,200,'登录成功')
        reponse=self.approveApi.approvequery(self.session)
        self.assertEqual(200,reponse.status_code)
        #self.assertEqual('-1',reponse.json().get('is_email_open'))