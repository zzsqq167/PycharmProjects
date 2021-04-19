import logging,requests
import unittest,random
from api.logAPI import logAPI
from api.trustAPI import trustApi
from utils import assertEqual_utils
from bs4 import BeautifulSoup
class trust(unittest.TestCase):
    def setUp(self):
        self.logApi=logAPI()
        self.trustApi=trustApi()
        self.session=requests.Session()

        self.phone='13798987191'
        self.password='test123'

    def tearDown(self):
        self.session.close()

    def test01_trust(self):
        reponse=self.logApi.loginenroll(self.session,self.phone,'test123')
        assertEqual_utils(self,reponse,200,200,'登录成功')
        print(reponse.json())

        reponse=self.trustApi.trustapi(self.session)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual(200,reponse.json().get('status'))

        form_data=reponse.json().get('description').get('form')

        soup = BeautifulSoup(form_data,'html.parser')
        thrid_url=soup.form['action']
        input_data={}
        for input in soup.find_all('input'):
             input_data.setdefault(input['name'],input['value'])
        #print(input_data)

        reponse = self.session.post(thrid_url,data=input_data)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual('UserRegister OK',reponse.text)


    def test02_veritycode(self):

        reponse = self.logApi.loginenroll(self.session, self.phone, self.password)
        assertEqual_utils(self, reponse, 200, 200, '登录成功')
        #获取验证码图片
        r=random.random()
        reponse=self.trustApi.veritycode(self.session,str(r))
        print(reponse.text)
        self.assertEqual(200,reponse.status_code)

        #请求充值
        reponse=self.trustApi.recharge(self.session)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual(200,reponse.json().get('status'))

        #请求第三方接口
        form_data=reponse.json().get('description').get('form')
        print(form_data)
        soup=BeautifulSoup(form_data,'html.parser')
        frist_url=soup.form['action']
        print('action=',frist_url)
        data={}
        for input in soup.find_all('input'):
            data.setdefault(input['name'],input['value'])
        print(data)

        reponse=self.session.post(frist_url,data=data)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual('UserRegister OK',reponse.text)


    def test03_recharge(self):
        reponse=self.logApi.loginenroll(self.session,self.phone,self.password)
        assertEqual_utils(self,reponse,200,200,'登录成功')

        r=random.randint(8888888,10000000)
        reponse=self.trustApi.veritycode(self.session,str(r))
        self.assertEqual(200,reponse.status_code)

        reponse=self.trustApi.recharge(self.session)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual(200,reponse.json().get('status'))

        form_data=reponse.json().get('description').get('form')
        soup=BeautifulSoup(form_data,'html.parser')
        Fried_url=soup.form['action']

        data={}
        for input in soup.find_all('input'):
            data.setdefault(input['name'],input['value'])
        reponse=self.session.post(Fried_url,data=data)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual('UserRegister OK',reponse.text)