# class LittleBell:
#     def sound(self):
#         print('ding')

# bell = LittleBell()
# bell.sound()

# Задачи:

# class Button:
#     def __init__(self):
#         self.count = 0

#     def click(self):
#         self.count += 1

#     def click_count(self):
#         return self.count

#     def reset(self):
#         self.count = 0

# button = Button()
# button.click()
# button.click()
# print(button.click_count())
# button.click()
# button2 = Button()
# button2.click()
# print(button.click_count())
# button.reset()
# print(button.click_count())
# print(button2.click_count())

# Напишите класс Balance для описания весов с двумя чашами. 
# На левую и правую чашу объекта будут добавляться грузы с различным весом, 
# ваша задача определить положение чаш.

# Метод add_right принимает целое число — вес, положенный на правую чашу весов, 
# add_left — на левую чашу. Метод result должен возвращать символ =, 
# если вес на чашах одинаковый, R — если перевесила правая, L — если перевесила левая.

# Формат ввода
# Каждый тест представляет собой код, в котором будет использоваться ваш класс. 
# Файл c решением не обязательно называть solution.py, он будет переименован автоматически. 
# Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

# class Balance:
#     def __init__(self):
#         self.left = 0
#         self.right = 0

#     def add_right(self, weight):
#         self.right += weight

#     def add_left(self, weight):
#         self.left += weight

#     def result(self):
#         if self.left == self.right:
#             return '='
#         elif self.left < self.right:
#             return 'R'
#         else:
#             return 'L'

# balance = Balance()
# balance.add_right(10)
# balance.add_left(9)
# balance.add_left(2)
# print(balance.result())
# balance2 = Balance()
# balance2.add_right(2)
# balance2.add_left(1)
# print(balance2.result())

# Напишите класс OddEvenSeparator, в который можно добавлять числа, получая потом отдельно чётные и нечётные. 
# Числа добавляются в объект с помощью метода add_number. Методы even и odd должны возвращать 
# списки чётных и нечётных чисел соответственно. Числа в списке должны идти в том же порядке, 
# что и при добавлении в объект.

class OddEvenSeparator:
    def __init__(self):
        self.list_obj = []
    
    def add_number(self, num: int):
        self.list_obj.append(num)
    
    def even(self):
        res_list = []
        for item in self.list_obj:
            if not item % 2:
                res_list.append(item)
        return res_list

    def odd(self):
        # res_list = []
        # for item in self.list_obj:
        #     if item % 2 != 0:
        #         res_list.append(item)
        return list(filter(lambda x: x % 2, self.list_obj))

x = OddEvenSeparator()
x.add_number(1)    
x.add_number(2)    
x.add_number(3)    
x.add_number(4)

print(x.even())
print(x.odd())

#

# class BingBell:
#     def __init__(self):
#         self.flag = True

#     def sound(self):
#         if self.flag:
#             print('ding')
#             self.flag = False
#         else:
#             print('dong')
#             self.flag = True

# x = BingBell()
# x.sound()
# x.sound()
# x.sound()

# 

class MinMax:
    def __init__(self):
        self.list_obj = []

    def add_sent(self, text: str):
        text_list = text.split()
        self.list_obj.extend(text_list)

    def short(self):
        count = 999
        for item in self.list_obj:
            if len(item) < count: count = len(item)
        return (lambda x: len(x) == count, self.list_obj)

