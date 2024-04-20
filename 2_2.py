# Найти самое длинное слово из массива. Реализовать двумя видами циклов
arr = input().split()
maxlen = len(arr[0])
maxword = arr[0]
# 1
for i in range(1, len(arr)):
    if len(arr[i]) > maxlen:
        maxlen = len(arr[i])
        maxword = arr[i]
'''
# 2
i = 1
while i < len(arr):
    if len(arr[i]) > maxlen:
        maxlen = len(arr[i])
        maxword = arr[i]
'''
print(maxword, maxlen)
