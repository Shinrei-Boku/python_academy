import csv

list_seq = []
list_name = []
list_total = []

#文字化け:utf-8-sig
with open("./file/lesson.csv", "r", encoding="utf-8-sig") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        #print(row)
        list_seq.append(row["seq"])
        list_name.append(row["name"])
        total = int(row["国語"]) + int(row["数学"]) + int(row["社会"])
        list_total.append(total)

with open('./file/lesson02.csv', 'w', encoding="utf-8-sig", newline="") as csv2_file:
    fieldnames= ['seq','name','合計']
    writer = csv.DictWriter(csv2_file, fieldnames= fieldnames)
    writer.writeheader()

    for i in range(0,len(list_seq)):
        writer.writerow({"seq":list_seq[i], "name":list_name[i], "合計":list_total[i]})

with open("./file/lesson02.csv", "r", encoding="utf-8-sig") as csv_file_read:
    csv2_reader = csv.DictReader(csv_file_read)
    for row in csv2_reader:
        print(row)
    
    
    

    