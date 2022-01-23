import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="student_record")
cursor = connection.cursor()

try:
    with connection.cursor() as cursor:
        cursor.execute('select * from students')
        
        result =    cursor.fetchall()
        
        for x in result:
            print(x);A
 
finally:
    connection.close()