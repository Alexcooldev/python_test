# Ќапишите класс, который будет содержать магический метод,
# который срабатывает при оборачивании объекта в число.
class Hi:
    def __int__(self):
        return 37


my_object = Hi()
number = int(my_object)
print(number)

