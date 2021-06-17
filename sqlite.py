import sqlite3
import csv

con = sqlite3.connect("testdb")
curs = con.cursor()
curs.execute("drop table M_EMPLOYEE")
curs.execute("CREATE TABLE M_EMPLOYEE(EMPLOYEE_ID int PRIMARY KEY, EMPLOYEE_NAME string)")
curs.execute('insert into M_EMPLOYEE (EMPLOYEE_ID,EMPLOYEE_NAME) values (202001,"boku-shinrei")')
curs.execute('insert into M_EMPLOYEE (EMPLOYEE_ID,EMPLOYEE_NAME) values (202002,"shinrei-boku")')
con.commit()
curs.execute("select * from M_EMPLOYEE")
l = curs.fetchall()
con.close()

with open("./kreisacademy/sqlite.csv", "w", encoding="utf-8-sig", newline="") as csv_file:
    filedname = ["employee_id", "employee_name"]
    writer = csv.DictWriter(csv_file,fieldnames=filedname)
    writer.writeheader()
    for i in l:
        writer.writerow({"employee_id":i[0], "employee_name":i[1]})

with open("./kreisacademy/sqlite.csv", "r", encoding="utf-8-sig") as csv_file_read:
    csv2_reader = csv.DictReader(csv_file_read)
    for row in csv2_reader:
        print(row)