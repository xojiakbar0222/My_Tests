""" 3 """
def toq_juft(a):
    "Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"
    if a % 2 == 0:
        print(f'{a} soni juftdir')
    elif a % 2 == 1:
        print(f' {a} soni toqdir')

c = int(input('c = '))

toq_juft(c)