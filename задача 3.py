import re


text = input('введите текст ')

# список слов текста, созданный с помощью регулярного выражения
list_of_words = re.findall(r'\w+', text.lower())

word_count = {} # создаём словарь, в который будем заносить данные формата: слово: кол-во его повторений в тексте

# Подсчитываем слова
for word in list_of_words:
    if word in word_count:
        word_count[word] += 1  # Увеличиваем счетчик, если слово уже есть
    else:
        word_count[word] = 1   # Добавляем новое слово со счетчиком 1

top_5_of_the_most_repeated_words = []

# проходимся по словам, добавляя в топ списки формата: [кол-во слов в тексте, слово]
# для простоты сортировки
for word, count in word_count.items():
    top_5_of_the_most_repeated_words.append([count, word])

# сортируем по убыванию количества повторений слова
top_5_of_the_most_repeated_words.sort(reverse=True)

num = 1 # переменная для нумерации позиций в топе

# извлекаем данные из списка слов и выводим построчно места в топе
for count, word in top_5_of_the_most_repeated_words[:5]:
    print(f'{num}) {word} - повторяется {count} раз')

    num += 1