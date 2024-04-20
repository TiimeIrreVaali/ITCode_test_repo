# Вывести каждую букву строки в обратном порядке без использования reversed() или [::-1]
s = input()
void = ""
for i in s:
    void = i + void
print(void)
