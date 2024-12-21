import re

with open("task2.html", "r", encoding="utf-8") as f:
    content = f.read()

color_patterns = [
    r"#[0-9a-fA-F]{3,6}\b", r"rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)",  
    r"\b[a-zA-Z]+\b"]

colors = []
for pattern in color_patterns:
    colors.extend(re.findall(pattern, content))


print(f"Найденные цвета: {colors}")
