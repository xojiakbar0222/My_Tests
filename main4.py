""" 4 """
def max_output(a, b):
    "Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya"
    if a>b:
        return a
    elif a == b:
        return 'Teng'
    else:
        return b

x = int(input('x = '))
y = int(input('y = '))

print(f'{x} va {y} sonlardan kattasi {max_output(x, y)}')
