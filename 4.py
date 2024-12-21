import re


with open('task_add.txt', 'r', encoding='utf-8') as file:
    content = file.read()

dates = re.findall(r"\b(\d{2,4}[./-]\d{2,4}[./-]\d{2,4})", content)
emails = re.findall(r'\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})', content)
adresses = re.findall(r'\s(https?://[a-zA-Z0-9.-]+)', content)

if dates[:5]:
    print("Dates:")
    for date in dates:
        print(f'  {date}')

if emails[:5]:
    print("Emails:")
    for email in emails:
        print(f'  {email}')

if adresses[:5]:
    print("Webs:")
    for adress in adresses:
        print(f'  {adress}')
