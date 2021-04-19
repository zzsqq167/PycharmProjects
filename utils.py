#import pymysql
import app,os,json
def assertEqual_utils(self,reponse,status_code,status,description):
    self.assertEqual(status_code,reponse.status_code)
    self.assertEqual(status,reponse.json().get('status'))
    self.assertEqual(description,reponse.json().get('description'))
# class sql_conn():
#     @classmethod
#     def conn(cls,SQL_name):
#         conn=pymysql.connect(app.SQL_URL,app.SQL_NUMBER,app.SQL_PASSWORD,SQL_name,autocommit=True)
#         return conn
#     @classmethod
#     def close(cls,cursor=None,conn=None):
#         if cursor:
#            cursor.close()
#         if conn:
#            conn.close()

    @classmethod
    def delete(cls,SQL_name,sql):
        try:
            conn=cls.conn(SQL_name)
            cursor=conn.cursor()
            cursor.execute(sql)
        except Exception as e:
            conn.rollback()

        finally:
            cls.close(cursor,conn)

def read_imgcode_data(file_name):
    file=app.BASE_DIR+os.sep + 'data'+ os.sep+file_name
    imgcode_data=[]
    with open(file,encoding='utf-8') as f:
        imgcode_case_data = json.load(f)
        imgcode_case_data=imgcode_case_data.get('test_login_img_code_data')

        for i in imgcode_case_data:
            imgcode_data.append((i.get('type'),i.get('status_code')))
        print('imgcode_data={}'.format(imgcode_data))
    return imgcode_data

def read_registers_data(file_name):
    file=app.BASE_DIR+os.sep+'data'+os.sep+file_name
    with open(file,encoding='utf-8') as f:
        file_data =json.load(f)
        register_data=file_data.get('test_register_data')
        register_daildata=[]
        for i in  register_data:
            register_daildata.append((i.get('phone'),i.get('password'),i.get('verifycode'),i.get('phone_code'),i.get('dy_server'),i.get('invite_phone'),i.get('status_code'),i.get('status'),i.get('description')))
        print('registerdate={}'.format(register_daildata))
    return register_daildata


def read_param_data(file_name,test_data,data_params):
    file = app.BASE_DIR+os.sep+'data'+os.sep+file_name
    with open(file,encoding='utf-8') as f:
        testdata=json.load(f)
        test_dail_date=testdata.get(test_data)
        datil_data=[]
        for i in test_dail_date:
            data_param=[]
            for j in data_params.split(','):
                data_param.append(i.get(j))
            datil_data.append(data_param)
        return datil_data