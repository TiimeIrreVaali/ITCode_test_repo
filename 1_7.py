# Создайте список-матрешку. Выведите на экран конечную строку.
task_list = [11, [1.6, [1+2j, [[], 25, "Иголка"]]]]
res = []
res.append(task_list[0])
res.append(task_list[1][0])
res.append(task_list[1][1][0])
res.extend(task_list[1][1][1])
print(*res)
