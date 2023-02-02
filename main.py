from random import randint


# функция проверки корректности введенного числа
def is_valid(digit, large):
    return False if not digit.isdigit() or not large >= int(digit) >= 1 else True


# функция проверки корректности введенного наибольшего числа
def is_largest_valid(digit):
    return False if not digit.isdigit() else True


# функция игры
def game():
    my_num = input(f'Введите число от 1 до {largest_num}: ')

    # проверка введенной строки
    if not is_valid(my_num, largest_num):
        print(f'\nА может быть все-таки введем целое число от 1 до {largest_num}?')
        return True

    my_num = int(my_num)

    # ветвление приближающее к результату
    if my_num < random_digit:
        print('Ваше число меньше загаданного, попробуйте еще разок!\n')
    elif my_num > random_digit:
        print('Ваше число больше загаданного, попробуйте еще разок!\n')
    elif my_num == random_digit:
        print(f'Вы угадали c {count} попытки, поздравляем!\n')
        return False
    return True


# основная функция
if __name__ == '__main__':

    # приветствие
    print('Добро пожаловать в числовую угадайку')

    while True:
        largest_num = input('В каком промежутке играем от 1 до ')

        # проверка введенной строки
        if not is_largest_valid(largest_num):
            print('\nА может быть все-таки введем целое число?')
            continue

        largest_num = int(largest_num)

        random_digit = randint(1, largest_num)  # выбор случайного числа из промежутка 1 до largest_num
        count = 1  # счетчик попыток

        # основной цикл
        while game():
            count += 1

        # возможность продолжить игру
        if input('Хотите сыграть еще? Напишите "д" если ДА, любое другое значение если НЕТ: ').lower() != 'д':
            break
        print()

    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
