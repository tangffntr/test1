import pymysql
db=pymysql.connect(host='localhost',user='root',password='qweasd123',database='test')
cursor=db.cursor()
sql1='SELECT * FROM students'
sql2='SELECT * FROM students WHERE score >= 80;'
sql3='SELECT COUNT(*) FROM students;'
cursor.execute(sql3)
result1=cursor.fetchone()
result2=cursor.fetchmany()
result3=cursor.fetchmany(2)
result4=cursor.fetchall()
print(result1[0])