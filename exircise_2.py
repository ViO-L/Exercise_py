'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
На входе:
var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
На выходе:
3 5
'''
# import random
# var2 = '11 20 33 40 50'
# var3 = '10 20 30 40 50'
# var_1 = '5 4'
# unical_number = (set(var3.replace(" ", "")).intersection(set(var2.replace(" ", ""))))
# print(unical_number)
# print_list = list(unical_number)
# unical_number_sorted = sorted(print_list)
# result = " ".join(unical_number_sorted)
# print(result)

var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'
delimitr = " "
split_string = var3.split(delimitr)
split_string2 = var2.split(delimitr)
ununical_number = (set(split_string).intersection(set(split_string2)))
print_list = list(ununical_number)
unical_number_sorted = sorted(print_list)
result = " ".join(unical_number_sorted)
print(result)

