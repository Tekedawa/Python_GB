# Task 1
def first_func(var_1, var_2):
    if var_2 == 0:
        try:
            var_1 / var_2
        except ZeroDivisionError:
            print("Деление на 0")
    else:  
        var_1 / var_2
        return var_1 / var_2
        
print(first_func(int(input("Введите первое число: ")), int(input("Введите второе число: "))))

# Task 2
def questionnaire():
    name = input("Введите имя: ")
    second_name = input("Введите фамилию: ")
    year_of_birth = int(input("Введите год рождения: "))
    city = input("Введите название города: ")
    email = input("Введите адрес электронной почты: ")
    phone = int(input("Введите номер телефона: "))
    ques = f'{name} {second_name} {year_of_birth} {city} {email} {phone}'
    return ques
    
quest = questionnaire()
print (f'Привет - {quest}')


#Task 3
def third_1_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3 - min(var_1, var_2, var_3)
print(third_1_func(10, 20, 30))"""

# Task 3.1
"""def third_func (list_val):
    list_val.sort() 
    var_d = list_val[-1] + list_val[-2]
    return var_d
print (third_func ([20, 50, 40, 60, 30, 10]))
# Вариант сложнее, но точнее. 

#Task 4
def fourth_func (var_a, var_b):
    return (var_a ** var_b)
print(fourth_func(int(input("Введите первое число: ")), int(input("Введите второе число: "))))

#Task 4.1
def fourth_func(var_b, var_c):
  var_a = 1
  if var_c >= 0:
    for i in range(0, var_c):
        var_a *=var_b
    return var_a
  else:
    for i in range(var_c, 0):
        var_a /=var_b
    return var_a
total = fourth_func(float(input("Введите первое число: ")),int(input("Введите второе число: ")))  
print(total)

# Task 5

def fifth_func(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag

general = 0

while True:
    numbers = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = fifth_func(*numbers)
    general += sum
    print(f'сумма {general}')

    if stop_flag:
        break

# Task 6
def Capitalize(S):
    d=''
    for i in range(len(S)):
        c=S[i]
        if c.isalpha() and i == 0:
            d += c.upper()
        elif c.isalpha() == True and S[i-1].isalpha() == False :
            d += c.upper()
        elif c.isupper() == True and S[i-1].isalpha() == True :
            d += c.lower()
        else:
            d += S[i]
    return(d)
S = input()
print (Capitalize(S))
    
        