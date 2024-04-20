# Даны множества студентов и рабочих.
# Вывести: 1) всех; 2) кто и учится, и работает; 3) кто только работает и не учится;
# 4) кто либо только учится, либо только работает.
students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}
# 1
print(*students | employees)
print(*students.union(employees))
# 2
print(*students & employees)
print(*students.intersection(employees))
# 3
print(*employees - students)
print(*employees.difference(students))
# 4
print(*students ^ employees)
print(*students.symmetric_difference(employees))
