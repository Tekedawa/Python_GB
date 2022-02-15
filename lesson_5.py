# Task 1
my_file = open('task_1.txt', 'w')
text = input('Введите текст \n')
while text:
    my_file.writelines(text)
    text = input('Введите текст \n')
    if not text:
        break

my_file.close()
my_file = open('task_1.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()

# Task 2
my_f = open('task_2.txt', 'r')
content = my_f.read()
print(f'Содержимое файла: \n {content}')
my_f = open('task_2.txt', 'r')
content = my_f.readlines()
print(f'Количество строк в файле - {len(content)}')
my_f = open('task_2.txt', 'r')
content = my_f.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} -й строки {len(content[i])}')
my_f = open('task_2.txt', 'r')
content = my_f.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_f.close()

# Task 3
with open('task_3.txt', 'r') as my_file:
    salary = []
    surname = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           surname.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {surname}, средний оклад {sum(map(int, salary)) / len(salary)}')


# Task 4

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file_task = []
with open('task_4.txt', 'r') as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        new_file_task.append(rus[i[0]] + ' ' + i[1])
        new_file_task = [line.rstrip() for line in new_file_task]
    print(new_file_task )
    f_obj.close()

with open('task_4_new.txt', 'w') as f_obj_new:
    f_obj_new.writelines(new_file_task )
    f_obj_new.close()

# Task 5

def count():
    try:
        with open('task_5.txt', 'w+') as myfile_obj:
            numbers = input('Введите цифры через пробел \n')
            myfile_obj.writelines(numbers)
            my_numbers = numbers.split()

            print(sum(map(int, my_numbers)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка при вводе данных')
count()

#Task 6

sub = open("task_6.txt", encoding='utf-8')
subject = sub.read().split("\n")

dict = {}

for i in subject:
    key = i.split(" ")[0]
    value = i.split(" ")[1:]
    dict[key] = value

print("\n<< Общее количество занятий по предметам >>")
for i in dict:
    list = dict[i]
    sum = 0
    for j in range(0, len(list)):
        sum += int(list[j])
    print(i, ":", sum)
sub.close()

# Task 7

import json
profit_dict = {}
companies_profit = {}
i = 0
profit = 0
profit_average = 0

with open('task_7.txt', 'r') as task_7:
    for line in task_7:
        firm, type, revenue, costs = line.split()
        profit_dict[firm] = int(revenue) - int(costs)
        if profit_dict.get(firm) >= 0:
            profit = profit + profit_dict.get(firm)
            i += 1
    if i != 0:
        profit_average = profit / i
        print(f'Average profit:\n ' f' {profit_average:.2f}')
    else:
        print(f'All companies unprofitable')
    companies_profit = {'Average profit': round(profit_average)}
   #profit_dict.update(companies_profit)
    print(f'Profit each company: \n ' f' {profit_dict}')
    print(f'Average profit: \n ' f' {companies_profit }')

with open('file_7.json', 'w') as write_js:
    json.dump(profit_dict,  write_js)
    js_str = json.dumps(profit_dict)

    json.dump(companies_profit, write_js)
    js_str_2 = json.dumps(companies_profit )
    print(f'Created file json type with next content: \n '
          f' {js_str}\n'
          f'  {js_str_2}\n')