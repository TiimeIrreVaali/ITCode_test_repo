# Проверить, является ли строка палиндромом (зеркальная)
s = input()
s = s.casefold()  # для сравнения вне зависимости от регистра
rev_s = reversed(s)
if list(s) == list(rev_s):
   print("Строка - палиндром.")
else:
   print("Строка - не палиндром.")
