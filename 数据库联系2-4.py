# import _sqlite3
# conn=_sqlite3.connect('mrsoft.db')
# cursor=conn.cursor()
# # cursor.execute('create table user(id int(10) primary key,name varchar(20))')
# # cursor.execute('insert into user(id,name) values("1","MRSOFT")')
# # cursor.execute('insert into user(id,name) values("2","Andy")')
# # cursor.execute('insert into user(id,name) values("3","明日科技小助手")')
# result=cursor.execute('select * from user where id>1')
# result1=cursor.fetchone()
# result2=cursor.fetchmany(2)
# result3=cursor.fetchone()
# print(result1)
# print(result2)
# print(result3)
# cursor.close()
# # conn.commit()
# conn.close()
# import requests
# response =requests.get('http://www.baidu.com')
# print(response.status_code)
# print(response.url)
# print(response.headers)
# print(response.cookies)
# print(response.text)
# print(response.content)
# data={'world':'hello'}
# response= requests.post('http://httpbin.org/post',data=data)
# print(response.content)
