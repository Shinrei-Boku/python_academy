import sqlite3
import csv

#
# テーブル作成(CreateTable)
# travel_expensesテーブルの存在チェックを行い存在しない場合はcreateを行う。
#
def create_table(curs):
    # 今回登録用テーブル名
    # TABLE作成用DDL。
    ddl = "CREATE TABLE  {} (EMPLOYEE_ID int,YEAR int, MONTH int, DAY int, REMARKS string, AMOUNT int)".format(tablename)
    print(ddl)
    # tablenameのテーブル存在チェックSQL
    sql = "SELECT COUNT(*) FROM sqlite_master WHERE TYPE='table' AND name='{}'".format(tablename)
    curs.execute(sql)
    cnt = curs.fetchone()[0]
    if 0 != cnt:
        return
    #0件の場合はcreatetableを実行
    curs.execute(ddl)

#
# ===== 処理開始 ======

#読込用のCSVファイル（ヘッダ付き）
csv_file ="./kreisacademy/file/travel_expenses.csv"
#登録用DB
dbname = './testdb'
#登録用テーブル名
tablename = 'travel_expenses'

# 1.csvファイルをディクショナリで読み込む
with open(csv_file) as reder_csv_file:
    reader = csv.DictReader(reder_csv_file)

    # 2.sqlite（DB）操作の為の手続き　connection取得し、sql文実行の為のカーソルをオープン（取得）。
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()

    try:
        # 3.テーブル作成関数呼び出し（すでに存在している場合は作成は行わないように制御）
        create_table(curs)
        # 4. レコードを全削除
        curs.execute('DELETE FROM {}'.format(tablename))
        # 5.登録
        for row in reader:
            curs.execute('INSERT INTO ' + tablename +'("EMPLOYEE_ID","YEAR","MONTH","DAY","REMARKS","AMOUNT") values(?,?,?,?,?,?)',[int(row['ID']),row['YEAR'],row['MONTH'],row['DATE'],row['REMARKS'],row['MONEY']])
        # 全sql実行文に対してCommitを行う。
        conn.commit()
        #
        curs.execute("select trv.EMPLOYEE_ID, emp.EMPLOYEE_NAME, trv.YEAR, trv.MONTH, sum(AMOUNT) from travel_expenses AS trv \
                      left join WK_M_EMPLOYEE as emp on trv.EMPLOYEE_ID = emp.EMPLOYEE_ID \
                      group by trv.EMPLOYEE_ID, trv.YEAR, trv.MONTH \
                      order by trv.EMPLOYEE_ID ASC, trv.YEAR ASC, trv.MONTH ASC")
        month_list = curs.fetchall()    
        
    finally:
        # connectionクローズ
        conn.close()

#sql_travel_expenses_total.csvの新規
with open('./kreisacademy/file/sql_travel_expenses_total.csv', 'w', encoding="utf-8-sig", newline="") as csv_writer_file:
    fieldnames= ['ID','Name','YEAR','MONTH','TOTAL']
    writer = csv.DictWriter(csv_writer_file, fieldnames= fieldnames)
    writer.writeheader()

    for k in month_list:
        writer.writerow({"ID":k[0], "Name":k[1], "YEAR":k[2], "MONTH":k[3], "TOTAL":k[4]})

#sql_travel_expenses_total.csvの読込
with open("./kreisacademy/file/sql_travel_expenses_total.csv", "r", encoding="utf-8-sig") as csv_file_read:
    csv2_reader = csv.DictReader(csv_file_read)
    for row in csv2_reader:
        print(row)