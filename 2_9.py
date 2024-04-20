# Удалить все дубликаты из списка без использования дополнительных структур.
# Реализовать двумя видами циклов, для удаления можно использовать pop() либо del
test_list = ['вы', 'чё', 'дебилы', 'вы', 'чё', 'ебанутые', 'что', 'ли', 'вы', 'в', 'натуре', 'ебанутые']
# 1
'''
for i in range(len(test_list)):
    for j in range(len(test_list) - 1, i, -1):
        if test_list[i] == test_list[j]:
            test_list.pop(j)
print(test_list)
'''
# 2
loc = 0  # курсор
while loc < len(test_list):
    if test_list[loc] in test_list[:loc]:  # проверка дубликата на текущем положении курсора
        test_list.pop(loc)
    else:
        loc += 1  # суть в смещении курсора не циклом, а ручками, чтоб не выйти за границы списка
print(test_list)
