# Программа получает на вход строку, содержащую имя, отчество и фамилию человека
# Необходимо вывести фамилию и инициалы.
snp = input().split()
res = []
res.append(snp[0])
res.append(snp[1][0] + '.')
res.append(snp[2][0] + '.')
print(*res)
