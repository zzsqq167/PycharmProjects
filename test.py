data='phone,password,verifycode,phone_code,dy_server,invite_phone'
data_dict=[{'phone':'13798987191','password':'test123','verifycode':'8888','phone_code':'666666','dy_server':'on','invite_phone':''},
           {'phone':'13798987192', 'password': 'test123', 'verifycode': '8888', 'phone_code': '666666', 'dy_server': 'on', 'invite_phone': ''}]
print("date type={}".format(type(data)))

data_list =data.split(',')
data_value=[]
data_case_value=[]
print('data_list={}'.format(type(data_list)))
for i in data_dict:
    print('i={}'.format(i))
    data_value=[]
    for j in data_list:
       print('j={}'.format(i.get(j)))
       data_value.append(i.get(j))
    print('data_value={}'.format(data_value))
    data_case_value.append(data_value)
    print('data_case_value={}'.format(data_case_value))


