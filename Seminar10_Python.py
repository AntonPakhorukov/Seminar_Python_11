# class Auto:
#     # атрибуты класса
#     auto_name = "Lexus"
#     auto_model = "RX 350L"
#     auto_year = 2019
#
#     # методы класса
#     def on_auto_start(self):
#         print(f"Заводим автомобиль")
#
#     def on_auto_stop(self):
#         print("Останавливаем работу двигателя")
#
#
# a = Auto()
# # print(a)
# # print(type(a))
# # print(a.auto_name)
# # print(Auto.auto_name)
# a.on_auto_start()
# a.on_auto_stop()
# Auto.auto_name = 'Audi'
# print(a.auto_name)
# print(Auto.auto_name)

# class Auto:
#     # атрибуты класса
#     auto_count = 0

#     # методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1


# a = Auto()
# print(Auto.auto_count)
# a.on_auto_start('Audi', 'RS6', 2019)
# b = Auto()
# print(Auto.auto_count)
# b.on_auto_start('BMW', 'M5', 2020)
# print(Auto.auto_count)
# print(a.auto_name)
# print(b.auto_year)
# print(a)

class Auto:
    auto_count = 0

    def __init__(self, auto_name, auto_model, auto_year):
        print("Автомобиль заведен")
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1


a = Auto('Volvo', 'x90', 2015)
print(a.auto_year)

