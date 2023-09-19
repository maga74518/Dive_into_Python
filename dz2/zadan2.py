num = int(input('Введите число: '))
num2 = int(input('Введите систему счисления: '))
digits = '0123456789abcdefghijklmnopqrstuvwxyz'
b = ''

while num > 0:
    b = digits[num % num2] + b
    num //= num2
print(b)