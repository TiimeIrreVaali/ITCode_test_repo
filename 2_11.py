# Напечатать календарь месяца, предполагая, что месяц начинается в понедельник и имеет 31 день
weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
print(*weekdays)
table = []
week = []
for i in range(1, 32):
    if i < 10:
        week.append(str(i).rjust(2))
    else:
        week.append(i)
    if i % 7 == 0:
        table.append(week)
        week = []
        continue
table.append(week)
for week in table:
    print(*week)
