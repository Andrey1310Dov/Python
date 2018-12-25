/*наиболее интересное решение задачи, так как тут сразу будем читать из файл с текстом, и даты записывать в новый файл.
Тут нужно учитывать кодировку, чтобы понимать сколько байт весит один символ.
При помощи file.seek() мы будем перемещаться по байтам, пропуская ненужное количество итераций, если дата найдена.
Но чтобы использовать file.seek() и двигаться вперед и назад без проблем, не забываем открывать все в бинаре*/


import re

with open('text.txt', 'rb') as text_file:
    new_file = open("data.txt", "w")
    check_end_text = 0
    while True:
        symbol = text_file.read(1)
        if not symbol:
            break
        if symbol.isdigit():
            text_file.seek(-1, 1)
            symbol = text_file.read(10)
            symbol_to_write = symbol.decode('utf-8')
            if len(symbol_to_write) < 10:              
                break
            if re.findall(r'\d{4}-\d\d-\d\d', symbol_to_write): 
                symbol_to_write += "\n"
                new_file.write(symbol_to_write)
            else:
                text_file.seek(-9, 1)
    new_file.close()
