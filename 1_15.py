# Вывести пирамиду
n = int(input())  # этажность пирамиды
for i in range(n):
    print('X' + 'xx' * i + 'X')