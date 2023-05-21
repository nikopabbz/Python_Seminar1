# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*

# 385916 -> yes
# 123456 -> no

numberTicket = int(input("Введите шестизначный номер: "))
if numberTicket < 100000 or numberTicket > 999999:
    print ("Вы ввели не шестизначный номер")
else:
    a = numberTicket % 10
    numberTicket = numberTicket // 10
    b = numberTicket % 10
    numberTicket = numberTicket // 10
    c = numberTicket % 10
    sumLastNumber = a + b + c
    numberTicket = numberTicket // 10
    d = numberTicket % 10
    numberTicket = numberTicket // 10
    e = numberTicket % 10
    numberTicket = numberTicket // 10
    f = numberTicket % 10
    sumFirstNumber = d + e + f
if sumFirstNumber == sumLastNumber:
    print("У вас счастливый билет!")
else:
    print("У вас не счастливый билет :(")
