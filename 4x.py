import random
def generate_combination():
    number = random.randint(1, 10)
    color = random.randint(1, 2)
    return number, color
def check_guess(combination, guess_number, guess_color):
    correct_number, correct_color = combination
    if guess_number == correct_number and guess_color == correct_color:
        return True
    else:
        return False
def play_game():
    combination = generate_combination()
    attempts = 5
    while attempts > 0:
        guess_number = int(input("Угадайте номер (от 1 до 10): "))
        guess_color = int(input("Угадайте цвет (1 - красный, 2 - черный): "))
        if check_guess(combination, guess_number, guess_color):
            print("Поздравляю! Вы угадали комбинацию!")
            return
        print("Вы не угадали!")
        attempts -= 1
    print("Вы использовали все попытки. Правильная комбинация: номер -", combination[0], ", цвет -", combination[1])
play_game()