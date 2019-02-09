import operator

dict_sym = {} # Создаем словарь, куда запишем все символы и их количество
answer = [] # Список с ответом

with open('symbols.txt', 'r') as file: # Заполняем словарь, считывая файл
    data = file.read()
    for i in data:
        if i in dict_sym:
            dict_sym[i] += 1
        else:
            dict_sym[i] = 1
            
dict_s = sorted(dict_sym.items(), key=operator.itemgetter(1)) # Сортируем словарь по значениям
for i in dict_s[0:8]: # Записываем первые 8 самых редких символов
    answer.append(i[0]) 
print(answer) 
