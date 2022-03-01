# Task 1

from time import sleep

class TrafficLight:
    def __init__(self, color):
        self._color = color
    def running(self):
        for key_color, value in self._color.items():
            sleep(value)
            print(key_color)


traffic = TrafficLight(color={
    "Красный": 7,
    "Желтый": 2,
    "Зеленый": 7})
traffic.running()

# Task 2

class Road:
    _length = 20
    _width = 5000


    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.thickness = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.thickness / 1000
        print(f"Масса асфальта\n {self._length} м * {self._width} м * {self.weight} кг * {self.thickness} см = ", asphalt_mass, "т")
        print(f'Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} тонн асфальта')

road_calc = Road(40, 10000)
road_calc.asphalt_mass()

# Task 3

class Worker:
    name = str
    surname = str
    position = str
    wage = int
    bonus = int

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


position_1 = Position('Nikolay', 'Nikolaev', 'Python developer', 900000, 35000)
print(position_1.get_full_name(), position_1.get_total_income())

position_2 = Position('Ivan', 'Ivanov', 'Projct Manager', 130000, 60000)
print(position_2.get_full_name(), position_2.get_total_income())

position_3 = Position('Petr', 'Petrov', 'Business Analyst', 105000, 45000)
print(position_3.get_full_name(), position_3.get_total_income())

position_4 = Position('Sergei', 'Sergeev', 'Senior Python Developer', 140000, 70000)
print(position_4.get_full_name(), position_4.get_total_income())

position_5 = Position('Dmitriy', 'Dmitriev', 'QA engineer', 80000, 20000)
print(position_5.get_full_name(), position_5.get_total_income())

# Task 4

class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость = {self.speed}'

class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nВаша скорость превышает ограничение скорости! Ваша скорость = {self.speed}'
        else:
            return f'Ваша скорость {self.name} в пределах нормы'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
             return f'\nВаша скорость превышает ограничение скорости! Ваша скорость = {self.speed}'
        else:
            return f'Ваша скорость {self.name} в пределах нормы'

class PoliceCar(Car):
    pass


town = TownCar('Toyota Camry', 60, 'черная', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('направо'), town.turn('направо'), town.stop() + '\n')

sport = SportCar('Shevrolet Camaro', 170, 'синяя', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop() + '\n')

work = WorkCar('Ford Mondeo', 45, 'серебристая', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('налево'), work.stop() + '\n')

police = PoliceCar('Nissan GTR', 100, 'белая', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('налево'), work.turn('налево'), work.stop() + '\n')

# Task 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

pen = Pen('при помощи ручки.')
print(pen.draw())
pencil = Pencil('при помощи карандаша.')
print(pencil.draw())
handle = Handle('при помощи маркера.')
print(handle.draw())
