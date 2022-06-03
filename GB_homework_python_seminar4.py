'''
Домашняя работа Семинара 4

Задача 1.
Напишите программу, которая будет преобразовывать десятичное число 
в двоичное.

Пример:

45 -> 101101
3 -> 11
2 -> 10
'''

'''
print("Переведём десятичное число в двоичное")
decimal_number = int(input("Введите целое положительное "
                           "десяничное число: "))

def conversion_number(arg_num):
    if arg_num < 0: return "Ошибко, вы ввели отрецательное число"
    if arg_num == 0: return 0
    binary_num = ""
    while arg_num != 0:
        binary_num = str(arg_num % 2) + binary_num
        arg_num //= 2
    return binary_num

result = conversion_number(decimal_number)
print("Ответ: {}".format(result))
'''

'''
Задача 2.
Задайте число. Составьте список чисел Фибоначчи, в том числе для 
отрицательных индексов.

Пример:

для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

'''
print("Составим список из чисел Негафибоначчи и Фибоначчи")
num = int(input("Введите целое число: "))
res_list = []

def num_negafib(arg_count, arg_num1, arg_num2, arg_res_list):
    """
    Функция заполняет и выводит список из чисел Негафибоначчи
    """
    while arg_count >= 0:
        arg_count -= 1
        num_negafib(
            arg_count, arg_num2, arg_num1 - arg_num2, arg_res_list)
        arg_res_list.append(arg_num1)
        return arg_res_list


def num_fib(arg_count, arg_num1, arg_num2, arg_res_list):
    """
    Функция запускает функцию, которая заполняет список числами
    Негафибоначчи, и после добавляет в этот же список числа Фибоначчи
    """
    arg_res_list = num_negafib(
        arg_count, arg_num1, arg_num2, arg_res_list)
    for i in range(arg_count):
        arg_num1, arg_num2 = arg_num2, arg_num1 + arg_num2
        arg_res_list.append(arg_num1)
    return arg_res_list

res_list = num_fib(num, 0, 1, res_list)
print("Ответ:", res_list)
'''

'''
Задача 3.
Задайте строку из набора чисел. Напишите программу, которая покажет 
большее и меньшее число. В качестве символа-разделителя 
используйте пробел.
'''

print("Найдём в строке большее и меньшее число")
string_input = input("Введите целые числа разделяя их пробелом:\n")

def find_num_min_max(arg_string):
    """
    Эта функция принимает строку из набора чисел разделённых
    пробелом и возвращает мельшее и большее число
    """
    num_min = ""
    temp = ""
    for char in arg_string:
        if char == " ": break
        num_min += char
    num_min = int(num_min)
    num_max = num_min
    for c in arg_string:
        temp += c
        if c == " ":
            if int(temp) < num_min: num_min = int(temp)
            elif int(temp) > num_max: num_max = int(temp)
            temp = ""
    if int(temp) < num_min: num_min = int(temp)
    elif int(temp) > num_max: num_max = int(temp)
    return num_min, num_max

res_min, res_max = find_num_min_max(string_input)
print(f"Ответ:\nменьшее число {res_min} большее число {res_max}")

'''
Задача 4.
Задайте два целых числа. Напишите программу, которая найдёт 
НОК (наименьшее общее кратное) этих двух чисел.
'''