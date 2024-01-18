'''В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:

A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

Пример:


k = 'ноутбук'
# 12
# '''

# d = {1:'AEIOULNSTRАВЕИНОРСТ', 2:"DGДКЛМПУ", 3:"BCMPБГЁЬЯ", 4:"FHVWYЙЫ",\
#           8:"JXШЭЮ", 5:'KЖЗХЦЧ', 10:'QZЩФЪ'}

# k = 'ноутбук'

# if k[0].upper() in d:
#     summa = 0
#     for symbol in k:
#         for key, value in d.items():
#             if symbol.upper() in value:
#                 summa+=1
#     print(summa)


#
# rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'
#
# list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
#                 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
# list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
#                 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}
#
# word = input('Введите слово на русском или английском языке: ')
#
# if word[0].lower() in eng:
#     summa = 0
#     for letter in word:
#         for key, value in list_English.items():
#             if letter.upper() in value:
#                 summa += key
#     print(f'стоимость введенного английского слова = {summa}')
# else:
#     if word[0].lower() in rus:
#         summa = 0
#         for letter in word:
#
#             for key, value in list_Russian.items():
#                 if letter.upper() in value:
#                     summa += key
#     print(f'стоимость введенного русского слова = {summa}')"KЖЗХЦЧ": 5, "QZФЩЪ": 10}

# k = input('Введите слово: ')
# if k[0].lower() in dict_1:
#     summa = 0
#     for letter in dict_1:
#         for value, key in dict_1.items():
#             if letter.upper() in key:
#                 summa += value
#     print(f'стоимость введенного английского слова = {summa}')

# eng = 'qwertyuiopasdfghjklzxcvbnm'

# rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

# list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
#                 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
# list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
#                 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}


# k = 'ноутбук'

# eng = 'qwertyuiopasdfghjklzxcvbnm'

# rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

# list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
#                 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
# list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
#                 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}

# word = input('Введите слово на русском или английском языке: ')

# # if word[0].lower() in eng:
# summa = 0
# for letter in word:
#     for key, value in list_English.items():
#         if letter.upper() in value:
#             summa += key
#     print(f'стоимость введенного английского слова = {summa}')
# else:
#     if word[0].lower() in rus:
#         summa = 0
#         for letter in word:

#             for key, value in list_Russian.items():
#                 if letter.upper() in value:
#                     summa += key
#     print(f'стоимость введенного русского слова = {summa}')
k = 'ящерица'  
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: '', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)

letter = 'QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
point = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
word = k.upper()
summ = 0
for i in word:
    if i in letter:
        for j in point:
            if i in point[j]:
                summ = summ + j

print(summ)