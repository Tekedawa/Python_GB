# Task 1
class Matrix:
    def __init__(self, my_list:list):
        self.my_list = my_list

    def __str__(self):
        result = []
        for el in self.my_list:
            result.append(' '.join([str(i) for i in el]))
        return '\n'.join(result)

    def __add__(self, other):
        if len(self.my_list) == len(other.my_list):
            result = []
            for j, row in enumerate(self.my_list):
                new_list = list(map(lambda x, y: x + y, row, other.my_list[j]))
                result.append(new_list)
            return Matrix(result)
        else:
            return


Matrix_list_01 = [[31, 22], [37, 43], [51, 86]]
Matrix_list_02 = [[51, 72], [27, 93], [31, 16]]
Matrix_list_03 = [[3, 5, 32], [2, 4, 6], [-91, 64, -8]]
Matrix_list_04 = [[47, 28, 2], [26, 45, 36], [78, 14, 23]]
Matrix_list_05 = [[3, 5, 8, 3], [8, 3, 7, 1]]
Matrix_list_06 = [[34, 15, 28, 31], [48, 33, 73, 21]]


Matrix01 = Matrix(Matrix_list_01)
Matrix02 = Matrix(Matrix_list_02)
Matrix03 = Matrix(Matrix_list_03)
Matrix04 = Matrix(Matrix_list_04)
Matrix05 = Matrix(Matrix_list_05)
Matrix06 = Matrix(Matrix_list_06)

Matrix_sum_01 = Matrix01 + Matrix02
Matrix_sum_02 = Matrix03 + Matrix04
Matrix_sum_03 = Matrix05 + Matrix06


print(Matrix01, end='\n\n')
print(Matrix02, end='\n\n')
print(Matrix03, end='\n\n')
print(Matrix04, end='\n\n')
print(Matrix05, end='\n\n')
print(Matrix06, end='\n\n')

print(Matrix_sum_01, end='\n\n')
print(Matrix_sum_02, end='\n\n')
print(Matrix_sum_03)


#Task_2

class clothes:
    def __init__(self, V_size, H_height):
        self.V_size = V_size
        self.H_height = H_height

    @property
    def my_fabric(self):
        return f"Размер пальто  = {self.V_size}." \
            f" Рост для костюма = {self.H_height} метра."

S_fabric = clothes(48, 1.8)

print(f"Сумма затраченной ткани равна {S_fabric.V_size  * (1 / 6.5) + 0.5}" )
print(f"Сумма затраченной ткани равна {S_fabric.H_height * 2 + 0.3}")
print(f"Сумма затраченной ткани равна {S_fabric.V_size * (1 / 6.5) + 0.5 + S_fabric.H_height  * 2 + 0.3} метра")

print(S_fabric.my_fabric)



# Variant 2. Use class



from abc import ABC, abstractmethod

class cloth (ABC):
    def __init__(self, size = 0, height = 0):
        self.size = size
        self.height = height
    
    @abstractmethod
    def coat(self, size):
        pass
    @abstractmethod
    def costume(self, height):
        pass
    @abstractmethod
    def all_fabric (self, size, height):
        pass

class fabric(cloth):
    def coat(self):
        print(f"Сумма затраченной ткани равна {self.size * (1 / 6.5) + 0.5 } метра.")

    def costume(self):
        print(f"Сумма затраченной ткани равна {self.height  * 2 + 0.3} метра")
        
    def all_fabric(self):
        print(f"Сумма затраченной ткани равна {self.size * (1 / 6.5) + 0.5 + self.height  * 2 + 0.3} метра")

textile = fabric(48, 1.8)

textile.coat()
textile.costume()
textile.all_fabric()


#Task_3

class Cell:
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        return f'Размер клетки увеличился и равен: {self.value + other.value} клеточкам.'

    def __sub__(self, other):
        sub = self.value - other.value
        return f'Размер клетки уменьшился и равен: {sub} клеточкам.' if sub > 0 else 'Клетка полностью исчезла'

    def __truediv__(self, other):
        return f'Размер клетки уменьшился и равен: {self.value // other.value}.' 

    def __mul__(self, other):
        return f'Размер клетки уменьшился и равен: {self.value * other.value}.'

    def make_order(self, row):
        result = ''
        for el in range(int(self.value / row)):
            result += '*' * row + '\n'
        result += '*' * (self.value % row) + '\n'
        return f'Количество строк и элементов клетки: {result}.'


first_cell = Cell(25)
second_cell = Cell(5)
print(first_cell + second_cell)
print(first_cell - second_cell)
print(first_cell / second_cell)
print(first_cell * second_cell)
print(first_cell.make_order(7))