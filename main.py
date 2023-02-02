from random import randint


# функция проверки корректности введенного числа
def is_valid(digit):
    return False if not digit.isdigit() or not 100 >= int(digit) >= 1 else True


# основная функция
if __name__ == '__main__':

    # инициализация программы
    print('Добро пожаловать в числовую угадайку')
    random_digit = randint(1, 100)

    # основной цикл
    while True:
        num = input('Введите число от 1 до 100: ')

        # проверка введенной строки
        if not is_valid(num):
            print('\nА может быть все-таки введем целое число от 1 до 100?')
        else:
            num = int(num)

            # ветвление приближающее к результату
            if num < random_digit:
                print('Ваше число меньше загаданного, попробуйте еще разок!\n')
            elif num > random_digit:
                print('Ваше число больше загаданного, попробуйте еще разок!\n')
            elif num == random_digit:
                print('Вы угадали, поздравляем!\n')
                break
    
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
