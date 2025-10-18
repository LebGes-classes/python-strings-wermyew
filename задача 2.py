text = input('введите текст из слов на английском языке ')

list_of_words = []
word = ""
last_char = ''

# делаем split()
for char in text: # проходимся по каждому символу
    if char == ' ':
       if last_char != ',': # если между словами пробел
            if word: # добавляем только непустые строки
                list_of_words.append(word)
                word = ''
    elif char == '.' or char == ',': # если после слова точка или запятая, добавляем слово
        if word:
            list_of_words.append(word)
            word = ""
    else: # если символ относится к слову, добаляем его к слову
        word += char
    last_char = char # обновляем вспомогаельную переменную
# добавляем последнюю часть
if word:
    list_of_words.append(word)

k = 0 # создаём переменную для подсчёта длины самого длинного слова
ind = 0 # создаём переменную для обозначения индекса самого длинного слова в тексте
num = 0 # переменная, которая будет обозначать индекс слова в тексте слов
k_and_ind = [] # список для длины этого слова и его индекса

for word in list_of_words: # проходимся по словам текста
    if k < len(word): # если длина слова больше длины прежнего самого длинного
        k = len(word)  # обновляем информацию о длине самого длинного слова
        ind = num # обновляем информацию об индексе самого длинного слова в тексте
    num += 1 # увеличиваем индекс, так как берём следующее слово

word = list_of_words[ind] # самое длинное слово

# английский алфавит в разных регистрах
low_alph = 'abcdefghijklmnopqrstuvwxyz'
high_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

shifr_word = '' # будущее зашифрованное слово

# проходимся по индексам символов самого длинного слова
for char_ind in range(k):
    if word[char_ind] in high_alph: # шифруем большие буквы, если они есть в слове
        shifr_word += high_alph[(high_alph.index(word[char_ind]) + k) % 26]
    elif word[char_ind] in low_alph: # шифруем букв нижнего регистра, если они есть
        shifr_word += low_alph[(low_alph.index(word[char_ind]) + k) % 26]
    else:
        shifr_word += word[char_ind]

# выводим зашифрованный текст посимвольно до самого длинного слова
for symb_ind in range(text.index(word)):
    print(text[symb_ind], end='')

# вместо самого длинного слова вписываем зашифрованное
print(shifr_word, end='')

# выводим зашифрованный текст посимвольно от последней буквы зашифрованного слова до конца текста
for symb_ind in range(text.index(word) + len(word), len(text)):
    print(text[symb_ind], end='')

print(' - зашифрованный текст') # пояснение для пользователя
print(k, '- число К') # число К