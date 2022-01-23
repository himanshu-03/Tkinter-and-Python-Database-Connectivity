import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="student_record")
cursor = connection.cursor()

try:
    with connection.cursor() as cursor:
        cursor.execute('update students set name = 'Shiv' where id = 45')
 
finally:
    connection.close()