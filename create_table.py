import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="student_record")
cursor = connection.cursor()

try:
    with connection.cursor() as cursor:
        cursor.execute('create table students(name varchar(150) not null, id int(20) not null primary key, department_name varchar(150) not null)')
 
finally:
    connection.close()
