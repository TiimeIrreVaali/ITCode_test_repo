# Замените в пользовательской строке все появления буквы h на букву H, кроме первого и последнего вхождения.
test = input()
indexes = []
first = test.find('h')
last = test.rfind('h')
mids = list(test[first+1:last])
for i in range(len(mids)):
    if mids[i] == 'h':
        mids[i] = 'H'
res = list(test[0:first+1]) + mids + list(test[last:])
print(''.join(res))
