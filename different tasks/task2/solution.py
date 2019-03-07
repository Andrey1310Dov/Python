letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open('names.txt', 'r') as file:
    data = file.read()
    data = data[1:len(data) - 1]
    list_of_words = data.split('","')
    list_of_words.sort()
    answers = []
    for word in list_of_words:
        sum_index = 0
        multiplication = 0
        for letter in word:
            sum_index += (letters.index(letter) + 1)
        multiplication = sum_index * (list_of_words.index(word) + 1)
        answers.append(multiplication)
    main_answer = sum(answers)

print(main_answer)

# Ответ main_answer = 871853874 
