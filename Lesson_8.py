# Task_1

from datetime import date


class Dates:
    def __init__(self, dates):
        self.dates = dates.split('-')

    @classmethod
    def type(cls, dates):
        
        try:
            day, month, year = [int(el) for el in dates.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Указана неправильная дата'

    @staticmethod
    def valid(dates):
        try:
            day, month, year = dates.split('-')
            date(int(year), int(month), int(day))
            return 'Указана корректная дата'
        except ValueError:
            return 'Указана неправильная дата'

user_date = '29-02-2021'
print(Dates.valid(user_date))
print(Dates.type(user_date))

#Task_2

class Division_Null:
    def __init__(self, dividend, devisor):
        self.dividend = dividend
        self.devisor = devisor

    @staticmethod
    def divide_null(dividend, devisor):
        try:
            return (dividend / devisor)
        except:
            return (f"Деление на ноль недопустимо")


div = 10
dev = 100

div_1 = 0
dev_1 = 10

div_2 = 10
dev_2 = 0


print(Division_Null.divide_null(div, dev))
print(Division_Null.divide_null(div_1, dev_1))
print(Division_Null.divide_null(dev_2, dev_2))
    
#Task_2.1

class Divide_Error(Exception):
    def __init__(self, num):
        self.num = num
        

user_div_1 = (input('Введите делимое: '))
user_div_2 = (input('Введите делитель: '))

try:
    user_div_1 = int(user_div_1)
    user_div_2 = int(user_div_2)
    if user_div_2 == 0:
        raise Divide_Error("Делить на ноль нельзя!")
    else:
        res = (user_div_1 / user_div_2)
except ValueError:
    print ("Вы ввели не число")
except Divide_Error as DivideError:
    print (DivideError)
else:
    print(f"Значение деления равно: {res}")
    
#Task_3

class list_Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                el = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(el)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                Cneck = input(f'Попробовать еще раз? Для продолжения введите "continue" или "y". Для выхода введите "stop" или "n" ').lower()

                if Cneck == 'y' or Cneck == 'continue' :
                    print(try_except.my_input())
                elif Cneck == 'n' or Cneck == 'stop':
                    return f'Вы вышли, текущий список {self.my_list}'
                else:
                    return f'Вы вышли'
try_except = list_Error()
print(try_except.my_input())

#Task_4,5,6

class Warehouse:
    __storage = []
    __summary = {}

    def push(self, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise Exception('Склад может принимать только оргтехнику')
        self.__storage.append(equipment)
        if self.__summary.get(equipment.type) is not None:
            self.__summary[equipment.type] += 1
        else:
            self.__summary.setdefault(equipment.type, 1)

    def report_items(self):
        for item in self.__storage:
            print(item)

    def report_total(self):
        for el, i in self.__summary.items():
            print(f'{el}: {i} шт')


class OfficeEquipment:
    def __init__(self, type: str, model: str, cost: float, sn: str):
        self.type = str(type)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, sn: str):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, sn)


class Scanner(OfficeEquipment):
    def __init__(self, model: str, cost: float, dpi: str, sn: str):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, sn)


class Copier(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str, velocity: int, sn: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__('Ксерокс', model, cost, sn)


if __name__ == '__main__':
    printer01 = Printer('Xerox Phaser', 12990, False, '30022777')
    printer02 = Printer('HP Ink Tank 115 2LB19A', 12499, True, ' 30040151')
    printer03 = Printer('Canon PIXMA G540', 24999, True, '30057807')
    printer04 = Printer('Epson L1300 (A3+)', 63499, True, '30025623')
    
    scanner01 = Scanner('Epson Perfection V19', 13999, '4800x4800', '30025691')
    scanner02 = Scanner('Plustek OpticFilm 8100', 25999, '7200x7200', '71427255')
    scanner03 = Scanner('Fujitsu fi-65F', 30199, '600x600', '7972400')
    scanner04 = Scanner('Kodak Alaris S2050', 48099, '600x600', '8123142')
    
    copier01 = Copier('HP DeskJet Plus Ink Advantage 6075 (5SE22C)', 11899, True, '1200x1200', 10, '71563486')
    copier02 = Copier('Brother DCP-T220 InkBenefit Plus', 19199, True, '1200x6000', 6, '71584205')
    copier03 = Copier('Canon PIXMA G2420', 17999, True, '600x1200', 9, '71578467')
    copier04 = Copier('Epson L3151', 22999, True, '1440x5760', 33, '71390312')
    copier05 = Copier('Xerox WorkCentre 3025BI', 22999, True, '600x600', 20, '71232203')


    warehouse = Warehouse()
    warehouse.push(printer01)
    warehouse.push(printer02)
    warehouse.push(printer03)
    warehouse.push(printer04)
    
    warehouse.push(scanner01)
    warehouse.push(scanner02)
    warehouse.push(scanner03)
    warehouse.push(scanner04)
    
    warehouse.push(copier01)
    warehouse.push(copier02)
    warehouse.push(copier03)
    warehouse.push(copier04)
    warehouse.push(copier05)

    warehouse.report_items()
    warehouse.report_total()
    
# Task_7

class ComplexNumber:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2
        self.complex_num = 'num_1 + num_2 * i'

    def __add__(self, other):
        print(f'\nСумма комплексных чисел равна')
        return f'Сумма равна: {self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i'

    def __mul__(self, other):
        print(f'\nПроизведение комплексных чисел равно')
        return f'Произведение равно: {self.num_1  * other.num_1 } + {self.num_2 * other.num_1  + self.num_1  * other.num_2} * i + {self.num_2 * other.num_2} * (i * i)'
    
    def __str__(self):
        print(f'\nЗначение комплексного числа')
        return f'complex_num = {self.num_1} + {self.num_2} * i'    


complex_num_1 = ComplexNumber(4, 8)
complex_num_2 = ComplexNumber(6, 11)
print(complex_num_1)
print(complex_num_2)
print(complex_num_1 + complex_num_2)
print(complex_num_1 * complex_num_2)