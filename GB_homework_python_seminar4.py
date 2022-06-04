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

'''
Задача 4.
Задайте два целых числа. Напишите программу, которая найдёт 
НОК (наименьшее общее кратное) этих двух чисел.
'''

print("Найдём наименьшее общее кратное двух чисел")
num1 = int(input("Введите первое положительное целое число: "))
num2 = int(input("Введите второе положительное целое число: "))

def decompose_into_prime_factors(arg_num):
    """
    В этой функции раскладываем число на простые множители и
    возвращаем список из них
    """
    arg_num = abs(arg_num)
    if arg_num == 0 or arg_num == 1: return [arg_num]
    res_list = []
    while arg_num != 1:
        count = 2
        while arg_num % count != 0: count += 1
        res_list.append(count)
        arg_num //= count
    return res_list

def comparing_lists(arg_list1, arg_list2):
    """
    В этой функции добовляем в первый список элементы второго,
    которые не пересекают первый
    """
    if arg_list1 == 0 or arg_list2 == 0: return 0
    res_list = arg_list1
    for char in arg_list1:
        for c in arg_list2:
            if char == c:
                arg_list2.remove(c)
                continue
    res_list += arg_list2
    return res_list

def find_smallest_common_multiple(combined_list):
    """
    В этой функции находим произведение элементов списка
    """
    if combined_list == 0: return 0
    res = 1
    for c in combined_list:
        res *= c
    return res

def checking_result(arg_num1, arg_num2, result):
    """
    В этой функции проверяем правельность решения
    """
    if result == 0: return False
    if result % arg_num1 == 0 and result % arg_num2 == 0:
        return True
    else:
        return False

list1 = decompose_into_prime_factors(num1)
list2 = decompose_into_prime_factors(num2)

print(f"Число {num1} разложенное на простые множители:\n{list1}")
print(f"Число {num2} разложенное на простые множители:\n{list2}")

res_comparing_lists = comparing_lists(list1, list2)

print("Общие множители:", res_comparing_lists)

smallest_common_multiple = find_smallest_common_multiple(
                          res_comparing_lists)

if num1 < 0 or num2 < 0:
    print("Все введённые отрецательные числа при расчётах менялись "
          "на положительные")
if checking_result(num1, num2, smallest_common_multiple):
    print("Наименьшее общее кратное:", smallest_common_multiple)
else:
    print("Ошибка")
