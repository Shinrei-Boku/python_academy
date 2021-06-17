import sqlite3
import csv

sqlite_list=[]

with open("./kreisacademy/WK_M_EMPLOYEE.csv", "r", encoding="utf-8-sig") as csv_file:
    reader = csv.DictReader(csv_file)   
    for row in reader:
        sqlite_list.append((int(row["EMPLOYEE_NO"]),row["EMP_NAME"],row["DEPARTMENT_KBN"],row["MAIL_ADDRESS"]))

con = sqlite3.connect("testdb")
curs = con.cursor()
curs.execute("drop table WK_M_EMPLOYEE")
curs.execute("CREATE TABLE WK_M_EMPLOYEE(EMPLOYEE_ID int PRIMARY KEY, EMPLOYEE_NAME string, DEPARTMENT_KBN string, MAIL_ADDRESS string)")
curs.executemany('INSERT INTO WK_M_EMPLOYEE VALUES (?,?,?,?)', sqlite_list)
con.commit()
curs.execute("select * from WK_M_EMPLOYEE")
print(curs.fetchall())
con.close()