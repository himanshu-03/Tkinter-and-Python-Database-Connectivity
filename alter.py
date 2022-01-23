import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="student_record")
cursor = connection.cursor()

try:
    with connection.cursor() as cursor:
        cursor.execute('alter table students add CGPI float(20) not null')
 
finally:
    connection.close()