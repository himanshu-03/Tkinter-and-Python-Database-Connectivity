import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             port='',
                             password='')
try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE student_record')
 
finally:
    connection.close()
