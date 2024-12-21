import re
import csv


with open("task3.txt", "r", encoding="utf-8") as f:
    content = f.read()

ids = re.findall(r"\b\d+\b", content)
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)
dates = re.findall(r"\d{4}-\d{2}-\d{2}", content)
urls = re.findall(r"https?://[^\s]+", content)
names = re.findall(r"\b[A-Z][a-z]+(?: [A-Z][a-z]+)?\b", content)

table = list(zip(ids, names, emails, dates, urls))

table_sorted = sorted(table, key=lambda x: int(x[0]))

with open("Output3.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Фамилия", "Email", "Дата", "Сайт"])
    writer.writerows(table_sorted)

print("Данные сохранены в файл Output3.csv")
