# Task 1
List = [24, b'text', 5.24, None, 'task', True, (12, 10)]
print (List)
for el in List:
    My_list = type (el)
    print (My_list)
    
# Task 2
Task_list = input ("Введите элементы списка: ").split()
for i in range(0, len(Task_list)-1, 2):
    Task_list[i], Task_list[i+1] = Task_list[i+1], Task_list[i]
print (Task_list)

# Task 3
month = int(input("Введите номер месяца: "))
season_dict = {1 : "Зима", 2 : "Зима", 3 : "Весна", 4 : "Весна", 5 : "Весна", 6 : "Лето", 7 : "Лето", 8 : "Лето", 9 : "Осень", 10 : "Осень", 11 : "Осень", 12 : "Зима"}
print (season_dict.get (month))

month_list = int(input("Введите номер месяца: "))
season_list= [0, "Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
season = season_list [month_list]
print (season)

# Task 4    
for ind, el in enumerate(input ("Введите элементы списка: ").split(), 1):
    element = el[0:11]
    print (ind, element)
    
# Task 5
Task5_my_list = [7, 5, 3, 3, 2]
number = (int(input ("Введите элементы списка: ")))
Task5_my_list.append (number)
Task5_my_list.sort (reverse = True)
print ("Пользователь ввел число ",number, ". Результат: ", Task5_my_list)

#Task 6
first_dict = [["название", input("Введите название: ")], ["цена", int(input("Введите цену: "))], ["количество", int(input("Введите количество: "))], ["единица измерения", input("Введите единицу измерения: ")]]
second_dict = [["название", input("Введите название: ")], ["цена", int(input("Введите цену: "))], ["количество", int(input("Введите количество: "))], ["единица измерения", input("Введите единицу измерения: ")]]
third_dict = [["название", input("Введите название: ")], ["цена", int(input("Введите цену: "))], ["количество", int(input("Введите количество: "))], ["единица измерения", input("Введите единицу измерения: ")]]

dict_1 = dict(first_dict )
dict_2 = dict(second_dict )
dict_3 = dict(third_dict )

tuple_1 = (1, dict(first_dict ))
tuple_2 = (2, dict(second_dict ))
tuple_3 = (3, dict(third_dict ))

#print(dict_1.get("название"))

analitic_1 = { "название" : [dict_1.get("название"), dict_2.get("название"), dict_3.get("название")]}
print (analitic_1)

analitic_2 = { "цена" : [dict_1.get("цена"), dict_2.get("цена"), dict_3.get("цена")]}
print (analitic_2)

analitic_3 = { "количество" : [dict_1.get("количество"), dict_2.get("количество"), dict_3.get("количество")]}
print (analitic_3)

analitic_4 = { "единица измерения" : [dict_1.get("единица измерения"), dict_2.get("единица измерения"), dict_3.get("единица измерения")]}
print (analitic_4)

    