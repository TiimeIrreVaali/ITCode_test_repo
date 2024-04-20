# Выведите количество слов в строке, не используя метод split()
import re

s = input()
count = len(re.findall(r'\w+', s))
print(count)
