#Создайте класс родитель. Дайте ему одно статическое поле и два динамических метода.
# Сделайте два класса-наследника, один из этих двух классов оставьте пустым.
# Создайте объект от каждого класса и вызовите методы.
class ParentClass:
    static_field = "Static Field"

    def dynamic_method1(self):
        print("Вызван динамический метод 1")

    def dynamic_method2(self):
        print("Вызван динамический метод 2")

class HeirClass1(ParentClass):
    pass  # Пустой класс-наследник

class HeirClass2(ParentClass):
    def dynamic_method3(self):
        print("Вызван динамический метод 3")

# Создаем объекты от каждого класса
obj1 = HeirClass1()
obj2 = HeirClass2()

# Вызываем методы для каждого объекта
obj1.dynamic_method1()
obj1.dynamic_method2()
obj2.dynamic_method1()
obj2.dynamic_method2()
obj2.dynamic_method3()



