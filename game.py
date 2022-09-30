from random import randint

def game():
    n = randint(4, 30)
    print(f'Начинаем игру! сейчас в куче {n} камней')
    while n > 1:
        n -= int(input("введите число камней, которые вы хотели бы взять(1, 2, 3)"))
        print(f'Теперь в куче {n} камней')
        if n < 1:
            print('выиграл компьютер')
            break
        if n > 1:
            if n == 3:
                n -= 2
                print('Выиграл компьютер')
                break
            elif n == 2:
                n -= 1
                print('Выиграл компьютер')
                break
            else:
                n -= randint(1, 3)
            print("Теперь мой ход)")
            print(f'Теперь в куче {n} камней')
            if n <= 1:
                print('Выиграл компьютер')
                break
        else:
            print("Выиграл пользователь")
            break
game()