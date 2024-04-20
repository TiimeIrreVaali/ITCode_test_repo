# У Вас есть строка, состоящая из двух слов, разделенных пробелом. Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.

first, second = input().split()
first, second = second, first
res = str(first) + ' ' + str(second)
print(res)
