import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="student_record")
cursor = connection.cursor()

try:
    with connection.cursor() as cursor:
        cursor.execute('delete from students where id = 45')
        connection.commit()
 
finally:
    connection.close()