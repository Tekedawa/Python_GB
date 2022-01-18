#task 1
price = 1
quantity = 3
print ("price", price)
print ("quantity", quantity)
number = int (input ("Введите номер продукта: ") )
product = (input ("Введите название продукта: "))
print ("number", number)
print ("product", product)

#Task2
#version 1
import time
sec = int (input ( "Введите количество секунд: "))
time_result = time.gmtime(sec)
result = time.strftime("%H:%M:%S",time_result)
print(result)

#version2
import datetime
sec =  int (input ( "Введите количество секунд: "))
result = datetime.timedelta(seconds = sec)
print(result)

#version3
sec0 = int(input ("Введите время в секундах: "))
sec = sec0 % (24 * 3600)
print (sec0)
hour = sec0 // 3600
sec %= 3600
min = sec // 60
sec %= 60
day = 0
'''if sec0 > 86400:
    day = hour // 24
    hour = hour - 24
    print ("Количество дней: ", day)
    print ("Количество часов: ", hour)
    print ("Количество минут: ", min)
    print ("Количество секунд: ", sec)
else:
    print ("Количество часов: ", hour)
    print ("Количество минут: ", min)
    print ("Количество секунд: ", sec)'''
if hour < 10:
   hour = "0" + str(hour)
if min < 10:
   min = "0" + str(min)
if sec < 10:
   sec = "0" + str(sec)
print (hour,":",min,":",sec)

#Task3
number = int(input('Введите число : '))
temp_number = str(number)
number2 = temp_number + temp_number
number3 = number2 + temp_number
sum = number + int(number2) + int(number3)
print (sum)

#Task4
number = int(input("Введите число: "))
max_number = number % 10
number = number // 10
while number > 0:
    if number%10 > max_number:
        #print(number)
        #print (max_number)
        max_number = number % 10
    number = number // 10
print(max_number)

#Task5
revenue = int(input('Введите значение выручки:'))
costs = int(input('Введите значение издержек:'))
profit = revenue - costs
if revenue > costs:
    print ('Поздравляем, компания прибыльная')
    profitability = profit / revenue * 100
    print ( profitability, " %")
    personal = int (input ("Введите количество персонала: "))
    PRE = profit / personal
    print (PRE, " рубля прибыли с одного сотрудника")
else:
    print ('К сожалению, прибыль не покрывает издержек. '
           'Необходимо проанализировать издержки, выявить долю постоянных издержек,'
           ' изучить на сто пошли переменные, узнать как можно сократить издержки. '
           'Необходимо увеличить прибыль. Уделить особое внимание анализц рынка, провести акции.'
           ' Изучить целевую аудиторию, возможно выйти на другую аудиторию и / или на другой рынок. '
           'Проанализировать ассортимент компании по ABC и XYZ анализам. Провести SWOT анализ. '
           'Полностью прошерстить бухгалтерскую отчетность.')

#Task6
distance = int(input('Введите дистанцию в км: '))
target = int(input('Введите цель в км: '))
day = 1
while distance < target:
    #print(distance, day)
    distance = distance * 1.1
    day += 1
else:
    day = day
    print ("На ", day,"-й день спортсмен достиг результата - не менее", target, " км")


