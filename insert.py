import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="student_record")
cursor = connection.cursor()

# queries for inserting values
insert1 = "INSERT INTO students(name, id, department_name, CGPI) VALUES('Himanshu Agarwal', '2', 'COMP', '9.96');"
insert2 = "INSERT INTO students(name, id, department_name, CGPI) VALUES('Yash Lohar', '56', 'IT', '9.20');"
insert3 = "INSERT INTO students(name, id, department_name, CGPI) VALUES('Khush Patel', '45', 'DS', '9.46');"
insert4 = "INSERT INTO students(name, id, department_name, CGPI) VALUES('Aayush Upadhyay', '66', 'AI&DS', '8.75');"

#executing the quires
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)
cursor.execute(insert4)

connection.commit()
connection.close()
