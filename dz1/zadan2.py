a, b, c = map(int, input('Введите длину сторон треугольника через пробел: ').split())

def existence_check(x, y, z):
    return True if (a + b > c) and (b + c > a) and (c + a > b) else False

def side_check(x, y, z):
    return 'равнобедренный' if x == y or y == z or x == z else 'разносторонний'

print('Треугольник существует и он ' + side_check(a, b, c) if existence_check(a, b, c) else 'Треугольник не существует')