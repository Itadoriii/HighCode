import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavestest',
                             cursorclass=pymysql.cursors.DictCursor)
