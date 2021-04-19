import unittest
from api.logAPI import logAPI
import random
import requests,logging,time
from utils import read_imgcode_data
from utils import read_registers_data
from utils import assertEqual_utils
from utils import read_param_data
from parameterized import parameterized
class login_code(unittest.TestCase):
    def setUp(self):
        self.loginAPI=logAPI()
        self.session=requests.Session()
        self.phone='13798987191'
        #注册成功手机号
        self.phone1='13798987152'
        self.phone2 ='13798987016'
        self.password='test123'
        self.imgVerifyCode='8888'

    def tearDown(self):
        self.session.close()

    @parameterized.expand(read_param_data('imgcode.json','test_login_img_code_data','type,status_code'))
    def test01_get_img_code(self,type,status_code):
        r=''
        if type == 'float':
            r=str(random.random())
        elif type =='int':
            r=str(random.randint(100000,900000))
        elif type=='str':
            r=''.join(random.sample('jfhjdfdjfndjfn',8))
        reponse=self.loginAPI.loginimgcode_url(self.session,r)
        self.assertEqual(status_code,reponse.status_code)

    # def test01_get_img_code_float(self):
    #     r=random.random()
    #
    #     reponse=self.loginAPI.loginimgcode_url(self.session,str(r))
    #
    #     self.assertEqual(200,reponse.status_code)
    #
    # def test02_get_img_code_int(self):
    #     r=random.randrange(1,10000)
    #     reponse=self.loginAPI.loginimgcode_url(self.session,str(r))
    #     self.assertEqual(200,reponse.status_code)
    #
    # def test03_get_img_code_parme_null(self):
    #
    #     reponse=self.loginAPI.loginimgcode_url(self.session,'')
    #     self.assertEqual(404,reponse.status_code)
    #
    # def test04_get_img_code_str(self):
    #     r=random.sample('jfefejbfjebfjekeorl',8)
    #     ran=''.join(r)
    #     reponse=self.loginAPI.loginimgcode_url(self.session,ran)
    #     self.assertEqual(400,reponse.status_code)
    #     print(ran)

    def test05_get_sms_code_scuess(self):
        #成功获取图片验证码
        r = random.random()
        reponse = self.loginAPI.loginimgcode_url(self.session, str(r))
        self.assertEqual(200, reponse.status_code)

        #发送短信验证码成功
        reponse=self.loginAPI.loginsmscode_url(self.session,self.phone,self.imgVerifyCode)
        assertEqual_utils(self, reponse, 200, 200, '短信发送成功')

    def test06_get_sms_code_fail(self):
        #图片验证码错误
        r = random.sample('jfefejbfjebfjekeorl', 8)
        ran = ''.join(r)
        reponse = self.loginAPI.loginimgcode_url(self.session,ran)
        self.assertEqual(400, reponse.status_code)

        # 发送短信验证码失败
        imimgVerifyCode_error='1234'
        reponse = self.loginAPI.loginsmscode_url(self.session,self.phone,imimgVerifyCode_error)
        assertEqual_utils(self,reponse,200,100,'图片验证码错误')

    def test07_get_sms_code_fail(self):
        # 成功获取图片验证码
        r=random.random()
        reponse=self.loginAPI.loginimgcode_url(self.session,str(r))
        self.assertEqual(200,reponse.status_code)
        #logging.info('get sms code {}'.format(reponse.json()))
        #手机号码为空，获取失败
        reponse=self.loginAPI.loginsmscode_url(self.session,'',self.imgVerifyCode)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual(100,reponse.json().get('status'))
    def test08_get_sms_code_fail(self):
        # 不获取图片验证码
        # 发送短信验证码成功
        reponse = self.loginAPI.loginsmscode_url(self.session, self.phone, '')
        assertEqual_utils(self, reponse, 200, 100, '图片验证码错误')


    @parameterized.expand(read_param_data('register.json','test_register_data','phone,password,verifycode,phone_code,dy_server,invite_phone,status_code,status,description'))
    def test02_get_register(self,phone,password,verifycode,phone_code,dy_server,invite_phone,status_code,status,description):
        # 成功获取图片验证码
        r = random.random()
        reponse = self.loginAPI.loginimgcode_url(self.session, str(r))
        self.assertEqual(200, reponse.status_code)

        # 发送短信验证码成功
        reponse = self.loginAPI.loginsmscode_url(self.session, phone, self.imgVerifyCode)
        assertEqual_utils(self, reponse, 200, 200, '短信发送成功')

        reponse=self.loginAPI.loginregister(self.session,phone,password,verifycode,phone_code,dy_server,invite_phone)
        print('register reponse={}'.format(reponse.json()))
        assertEqual_utils(self,reponse,status_code,status,description)

    def test09_get_register_success(self):
        # 成功获取图片验证码
        r = random.random()
        reponse = self.loginAPI.loginimgcode_url(self.session, str(r))
        self.assertEqual(200, reponse.status_code)

        # 发送短信验证码成功
        reponse = self.loginAPI.loginsmscode_url(self.session, self.phone1, self.imgVerifyCode)
        assertEqual_utils(self, reponse, 200, 200, '短信发送成功')

        reponse=self.loginAPI.loginregister(self.session,self.phone1,self.password,invite_phone='13798987198')
        #logging.info('the register reponse is {}'.format(reponse.json()))
        assertEqual_utils(self,reponse,200,200,'注册成功')

    def test10_get_register_fail(self):
         #成功获取图片验证码
         r=random.random()
         reponse=self.loginAPI.loginimgcode_url(self.session,str(r))
         self.assertEqual(200,reponse.status_code)

         #获取短信验证码失败(图片验证码错误)
         reponse=self.loginAPI.loginsmscode_url(self.session,self.phone2,imgVerifyCode='8889')
         assertEqual_utils(self, reponse, 200, 100, '图片验证码错误')

         #注册失败
         reponse=self.loginAPI.loginregister(self.session,self.phone2,self.password)
         assertEqual_utils(self,reponse,200,100,'验证码过期或无效，请重新获取')

    def test11_get_register_fail(self):
        #成功获取图片验证码
        r=random.random()
        reponse=self.loginAPI.loginimgcode_url(self.session,str(r))
        self.assertEqual(200,reponse.status_code)

        # 获取短信验证码
        reponse = self.loginAPI.loginsmscode_url(self.session, self.phone2, self.imgVerifyCode)
        assertEqual_utils(self, reponse, 200, 200, '短信发送成功')

        #注册失败（短信验证码错误）
        reponse=self.loginAPI.loginregister(self.session,self.phone2,self.password,phone_code='12345')
        assertEqual_utils(self,reponse,200,100,'验证码错误')

    def test12_get_register_fail(self):
         # 成功获取图片验证码
         r = random.random()
         reponse = self.loginAPI.loginimgcode_url(self.session, str(r))
         self.assertEqual(200, reponse.status_code)

         # 获取短信验证码
         reponse = self.loginAPI.loginsmscode_url(self.session, self.phone, self.imgVerifyCode)
         assertEqual_utils(self, reponse, 200, 200, '短信发送成功')

         # 注册失败（手机号码已注册）
         reponse = self.loginAPI.loginregister(self.session, self.phone, self.password)
         assertEqual_utils(self, reponse, 200, 100, '手机已存在!')

    # def test12_get_register_fail(self):
    #      # 成功获取图片验证码
    #      r = random.random()
    #      reponse = self.loginAPI.loginimgcode_url(self.session, str(r))
    #      self.assertEqual(200, reponse.status_code)
    #
    #      # 获取短信验证码
    #      reponse = self.loginAPI.loginsmscode_url(self.session, self.phone2, self.imgVerifyCode)
    #      assertEqual_utils(self, reponse, 200, 200, '短信发送成功')
    #
    #      # 注册失败（不同意条款）
    #      reponse = self.loginAPI.loginregister(self.session, self.phone2, self.password,dy_server='off')
    #      assertEqual_utils(self, reponse, 200, 200, '注册成功')

    def test13_get_enroll_success(self):
        reponse=self.loginAPI.loginenroll(self.session,self.phone,self.password)
        assertEqual_utils(self, reponse, 200, 200, '登录成功')

    def test14_get_enroll_fail(self):
        reponse=self.loginAPI.loginenroll(self.session,self.phone2,self.password)
        assertEqual_utils(self,reponse,200,100,'用户不存在')

    def test15_get_enroll_fail(self):
        reponse=self.loginAPI.loginenroll(self.session,self.phone,'')
        assertEqual_utils(self, reponse, 200, 100, '密码不能为空')



    # def test16_get_enroll_fail(self):
    #     reponse=self.loginAPI.loginenroll(self.session,self.phone,password='test1')
    #     assertEqual_utils(self, reponse, 200, 100,'密码错误1次,达到3次将锁定账户')
    #     reponse=self.loginAPI.loginenroll(self.session,self.phone,password='test1')
    #     assertEqual_utils(self, reponse, 200, 100,'密码错误2次,达到3次将锁定账户')
    #     reponse=self.loginAPI.loginenroll(self.session,self.phone,password='test1')
    #     assertEqual_utils(self, reponse, 200, 100,'由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录')
    #     print("Start : %s" % time.ctime())
    #     time.sleep(61)
    #     print("end : %s" % time.ctime())
    def test17_get_enroll_success(self):
        reponse=self.loginAPI.loginenroll(self.session,self.phone,self.password)
        assertEqual_utils(self, reponse, 200, 200, '登录成功')

    def test18_get_enroll_statu(self):
        reponse=self.loginAPI.loginstatu(self.session)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual('您未登陆！',reponse.json().get('description'))

    def test19_get_enroll_statu(self):
        reponse=self.loginAPI.loginenroll(self.session,self.phone,self.password)
        assertEqual_utils(self,reponse,200,200,'登录成功')
        reponse=self.loginAPI.loginstatu(self.session)
        self.assertEqual(200,reponse.status_code)
        self.assertEqual('OK',reponse.json().get('description'))
