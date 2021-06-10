import csv

l = []

#文字化け:utf-8-sig
with open("./file/lesson.csv", "r", encoding="utf-8-sig") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        row["合計"] = int(row["国語"]) + int(row["数学"]) + int(row["社会"])
        l.append({'seq':row['seq'],'name':row['name'], '合計':row['合計']})

with open('./file/lesson02.csv', 'w', encoding="utf-8-sig", newline="") as csv2_file:
    fieldnames= ['seq','name','合計']
    writer = csv.DictWriter(csv2_file, fieldnames= fieldnames)
    writer.writeheader()

    for i in l:
        writer.writerow({"seq":i["seq"], "name":i["name"], "合計":i['合計']})

with open("./file/lesson02.csv", "r", encoding="utf-8-sig") as csv_file_read:
    csv2_reader = csv.DictReader(csv_file_read)
    for row in csv2_reader:
        print(row)
    
    
    

    