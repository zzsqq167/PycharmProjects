import app
import requests
import os
class logAPI():
    def __init__(self):
        self.loginimgAPI_url=app.BASE_URL+'/common/public/verifycode1/'
        self.loginsmsAPI_url=app.BASE_URL+'/member/public/sendSms'
        self.loginregisterAPI_url=app.BASE_URL+'/member/public/reg'
        self.loginenrollApi_url=app.BASE_URL+'/member/public/login'
        self.loginstatu_url=app.BASE_URL+'/member/public/islogin'

    def loginimgcode_url(self,session,r):
        url=self.loginimgAPI_url+r
        reponse=session.get(url)
        return reponse
    def loginsmscode_url(self,session,phone,imgVerifyCode):
        url=self.loginsmsAPI_url
        data={'phone':phone,'imgVerifyCode':imgVerifyCode,type:"reg"}
        reponse = session.post(url,data=data)
        return reponse
    def loginregister(self,session,phone,password,verifycode='8888',phone_code='666666',dy_server='on',invite_phone=''):
        data={'phone':phone,
              'password':password,
              'verifycode':verifycode,
              'phone_code':phone_code,
              'dy_server':dy_server,
              'invite_phone':invite_phone}
        url=self.loginregisterAPI_url
        reponse=session.post(url,data=data)
        return reponse

    def loginenroll(self,session,phone,password):
        data={'keywords':phone,
              'password':password}
        url=self.loginenrollApi_url
        reponse=session.post(url,data=data)
        return reponse

    def loginstatu(self,session):
        url=self.loginstatu_url
        reponse=session.post(url)
        return reponse