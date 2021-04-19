import app
class trustApi():

      trustapi_url=app.BASE_URL+'/trust/trust/register'
      veritycode_url=app.BASE_URL+'/common/public/verifycode/'
      recharge_url=app.BASE_URL+'/trust/trust/recharge'

      def trustapi(self,session):

          reponse=session.post(self.trustapi_url)
          return reponse

      def veritycode(self,session,r):
          url=self.veritycode_url+r
          reponse=session.get(url)
          return reponse

      def recharge(self,session,amount='1000',valicode='8888'):
          data={'paymentType':"chinapnrTrust",
                'amount':amount,
                'formStr':"reForm",
                'valicode':valicode}
          reponse=session.post(self.recharge_url,data=data)
          return reponse

