num = int(input('Введите число от 1 до 100 тысяч: '))
def is_valid(x):
    if 0 < x < 10000:
        return x
    else:
        x = int(input('Вы ввели не правильное число! Введите число от 1 до 100000: '))
        return is_valid(x)

if is_valid(num):
    print('Число простое' if len([i for i in range(1, num+1) if num % i == 0]) == 2 else 'Число составное')