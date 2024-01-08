import random
set1 = {random.randint(1, 100) for i in range(10)}
set2 = {int(input('Введите число: ')) for i in range(10)}
q = set1 & set2
key = [1, 2, 3, 4, 'df', 5, 'rt', 'we', 6, 7]
y = dict(zip(key, q))
print(y)