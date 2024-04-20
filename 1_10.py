#Проверить, все ли числа в произвольной последовательности уникальны.
test = list(map(int, input().split()))
test_set = set(test)
if len(test) == len(test_set):
    print("Все числа уникальны")
else:
    print("Есть повторы")