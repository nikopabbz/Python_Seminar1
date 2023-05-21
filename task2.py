# Задача 2: Найдите сумму цифр трехзначного числа.
number = int(input("Введите трехзначное число: "))
if number < 100 or number > 999:
    print ("Вы ввели не трехзначное число")
else:
    a = number % 10
    number = number // 10
    b = number % 10
    number = number // 10
    c = number % 10
    print (a + b + c)