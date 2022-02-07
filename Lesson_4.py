#task1
from sys import argv
script, hours, rate, incentive = argv
salary = int(hours) * int(rate) + int(incentive)

print ("Количество отработанных часов: ", hours)
print ("Ставка в час: ", rate)
print ("Сумма премии: ", incentive)
print (f'(Количество отработанных часов * Ставка в час) + Сумма премии: {hours}  *  {rate}  +  {incentive}  = {salary}')
print ("Сумма заработной платы: ", salary)

#Task2
number_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list  = [i1 for i1, i2 in zip(number_list[1:], number_list[:-1]) if i1 > i2]
print(new_list)

#Task3
new_list = [el for el in range (20, 241)  if el %  20  ==  0 or el %  21 ==  0]
print (new_list)

print([el for el in range(20, 241) if el % 20 == 0 or el  % 21 == 0])

#Task4
number_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list  = [i for i in number_list if number_list.count(i) == 1]
print(new_list)

#Task5
from functools import reduce
list_5 = [el for el in range(100, 1001, 2)]
print("Список чётных чисел в диапазоне [100..1000]:\n", list_5)
print("\nПроизведение всех элементов списка:\n", reduce(lambda x,y: x*y, list_5))

#Task 6
from itertools import count

print("Итератор, генерирующий целые числа, начиная с указанного:")
# Включая 3
for el in count(3):
    if el > 10:
        break
    else:
        print(el)
        
from itertools import cycle

print("\nИтератор, повторяющий элементы некоторого списка, определенного заранее:")
num = 1
for value in cycle([1, 2, 3, 4]):
    if num > 10:
        break
    print(value)
    num += 1
    
#Task 7
def fact(n):
    temp = 1
    for el in range(1, n + 1):
        temp *= el
        yield temp
 
 
n = int(input("Укажите факториал какого числа Вы хотели бы узнать?\n")) 
for el in fact(n):
    print(el)
