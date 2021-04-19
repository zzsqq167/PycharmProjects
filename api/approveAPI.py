import app
class approveApi():
    approveApi_url=app.BASE_URL+'/member/realname/approverealname'
    getapprove_url=app.BASE_URL+'/member/member/getapprove'
    approvequery_url=app.BASE_URL+'/member/member/getapprove'

    def approve(self,session,realname,card_id):
        data={'realname': realname,
        'card_id': card_id}
        reponse=session.post(self.approveApi_url,data=data,files={'x':'y'})
        return reponse

    def approvequery(self,session,):

        reponse=session.post(self.approvequery_url)
        return reponse