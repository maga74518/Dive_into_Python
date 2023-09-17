for a in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    if a != 0:
        print('')
    for b in range(1, 10):
        print('%s * %s = %s\t\t\t' % (a[0], b, a[0] * b),
            '%s * %s = %s\t\t\t' % (a[1], b, a[1] * b),
            '%s * %s = %s\t\t\t' % (a[2], b, a[2] * b), )