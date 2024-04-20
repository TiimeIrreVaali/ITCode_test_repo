# Подсчет суммы всех четных чисел от 1 до n. Реализовать двумя видами циклов
n = int(input())
res = 0
# 1
for i in range(1, n):
    if i % 2 == 0:
        res += i
'''
# 2
i = 1
while i < n:
    if i % 2 == 0:
        res += i
'''
print(res)