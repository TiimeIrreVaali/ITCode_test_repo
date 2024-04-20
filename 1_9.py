# Соедините два списка и отсортируйте их. Затем удалите повторяющиеся элементы.
l1 = [2, 1, 3, 0]
l2 = [2, 3, 4, 5]
lst = l1 + l2
lst = sorted(lst)
print(lst)
lst = list(set(lst))
print(lst)
