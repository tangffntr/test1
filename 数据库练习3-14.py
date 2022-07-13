import pymysql
db=pymysql.connect(host='localhost',user='root',password='qweasd123',database='hello')
cursor =db.cursor()
cursor.execute('DROP TABLE IF EXISTS books')
sql="""
CREATE TABLE books(
id int(8) NOT NULL AUTO_INCREMENT,
name varchar(50) NOT NULL,
category varchar(50) NOT NULL,
price decimal(10,2) DEFAULT NULL,
publish_time date DEFAULT NULL,
PRIMARY KEY(id))
ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)
data=[('零基础学Python','Python','79.80','2018-5-20'),('Python从入门到精通','Python','69.80','2018-6-18')]
try:
    cursor.executemany('insert into books(name,category,price,publish_time) values(%s,%s,%s,%s)',data)
    db.commit()
except:
    db.rollback()


db.close()
