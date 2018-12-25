import sqlite3
import random
 
con = sqlite3.connect("mytable.db")  

cur = con.cursor()   				#cоздаем объект-курсор

#выполняем создание нужной таблицы
cur.execute("CREATE TABLE users (id,users)")
#создаем ссылки на нужные типы объектов
user = ''
id = 1
list_of_symbols = list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')   #из этих символово будем создавать псевдослучайные имена юзеров

for number in range(1000000):                                             #сколько нужно внести записей в базу данных, такой и range; в нашем случае 1 000 000
	user = ''.join([random.choice(list_of_symbols) for x in range(10)])     #имя юзера состоит из десяти символов, поэтому range(10)
	cur.execute("INSERT INTO users (id, users) VALUES (?, ?)" ,(id, user))  #вносим в таблицу id и user
	id += 1


cur.execute("SELECT * FROM users")        #выбираем все поля и записи                                     
                                          
result = cur.fetchall()                   #выводим результат
print(result)

cur.close()     				#закрываем объект-курсор
con.close()     				#закрываем соединение
