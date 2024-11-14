# إقرأ محتوى ملف
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# إكتب محتوى ملف
with open('example.txt', 'w', encoding='utf-8') as file: # للإضافة على محتوى الملف، غير 'w' إلى 'a'
    file.write("Welcome to CoddingHoddie")

# إكتب محتوى CSV
import csv

# إقرأ محتوى CSV
with open("scores.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

data = [
    ["الاسم", "العمر", "المدينة"],
    ["علي", 25, "القاهرة"],
    ["فاطمة", 30, "الرياض"]
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)
