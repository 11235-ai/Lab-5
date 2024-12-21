import re

with open("task1-en.txt", "r", encoding="utf-8") as f:
    content = f.read()

words = re.findall(r", ([а-яА-ЯёЁa-zA-Z]+)", content)
squares = re.findall(r"\[.*?\]", content)

print(f"Слова после запятой: {words}")
print()
print(f"Информация в квадратных скобках: {words}")
