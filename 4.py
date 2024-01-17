import random
n = random.randint(1,10)
x = random.randint(1,2)
i = 5
while i > 0:
    q = int(input('Угадайте номер (от 1 до 10): '))
    w = int(input('Угадайте цвет (1 - красный, 2 - черный): '))
    if q == n and w == x:
        print('Вы угадали!!!!')
        break
    else: print('Вы не угадали. Попробуйте еще раз')
    i -= 1
print('Вы использовали все попытки. Правильная комбинация: номер -',n, ', цвет -',x)