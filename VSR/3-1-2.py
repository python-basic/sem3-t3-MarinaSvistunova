# 3.2. Реализовать программу-игру «Угадай число», в которой для вывода на экран информации использовать метод format.

import random
def guess_num():
    num_rand = input("Введите граничные числа диапазона через пробел: ")
    num_rand = num_rand.split(' ')
    a, b = num_rand[0], num_rand[-1]
    guess_this = random.randint(int(a), int(b))
    print("Число загадано!\nВведите число: ")
    user_num = int(input())
    while (user_num != guess_this):
        if (user_num < guess_this):
            print("Загаданное число больше {}".format(user_num))
        else:
            print("Загаданное число меньше {}".format(user_num))
        user_num = int(input())
    print("Поздравляю! Вы угадали! Загаданое число: {}".format(str(guess_this)))

if __name__ == "__main__":
    user_text = input("Игра? Да или Нет? ")
    if (user_text == "Да" or user_text == "да"):
        guess_num()
    else:
        print("Пока!")
