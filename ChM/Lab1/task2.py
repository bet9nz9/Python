import re

fio = 'Батура Максим Юриевич'
print('Длинна строки: '+str(len(fio)))
arr_of_sliced_fio = re.split(r'\s|\t|\ ', fio)
print('Разделенная строка: ',arr_of_sliced_fio)
def count(char, word):
    counter = 0
    for i in word:
        if i == char:
            counter +=1
    return counter
print('Количество букв о в fio: '+str(count('о', fio)))
print('Количество букв e в fio: '+str(count('е', fio)))

fio2 = 'Батура\nМаксим\tЮриевич'
print('Длинна строки c переносами и табуляциями: '+str(len(fio2)))
