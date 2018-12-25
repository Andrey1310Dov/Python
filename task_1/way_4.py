#метод несколько иной, чем до этого, поэтому сначала импортируем нужные модули
import re
from itertools import islice

#создаем нужные ссылки на типы объектов
string_with_dates = "e1452-25-16ntriesareduebyJan1452-25-16uary4440-15-254th201at8:00pmreated2005-10-15byACMEInc.andassoci1425-12-15ates2345-14-12"
scrolls = []
n = 0
numbers = '1234567890'
x = '-'
ten_symbols = iter(string_with_dates) #создаем итератор, по нему пробегаемся циклом
for i in ten_symbols:
    if i in numbers:        
        if re.findall(r'\d{4}-\d\d-\d\d', string_with_dates[n:n + 10]):  #для сравнение в ход идет вновь регулярка
            scrolls.append(string_with_dates[n:n + 10])                  
            i = next(islice(ten_symbols, 9, 10), None)  #islice использует срез индекса, next помогает перскочить через лишние итерации
            n += 11
        else:
            n += 1
    else:
        n += 1
print(scrolls) #выводим даты
