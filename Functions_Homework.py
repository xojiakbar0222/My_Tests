# """ 1 va 2 """
#
# def personal_data(name, surname, email, age = None, country = None):
#     A = {
#         'ismi':name,
#         "familyasi":surname,
#         'pochtasi':email,
#         'yoshi':age,
#         'davlati': country
#     }
#
#     print(f'\n Ushbu insonning: ')
#     for i, j in A.items():
#         print(f'{i}:{j}')
#
# while True:
#     toxatatamizmi = input('Toxtaysizmi? (Ha/yoq):')
#     if toxatatamizmi.lower() == 'ha':
#         break
#     elif toxatatamizmi.lower()=='yoq':
#         name = input('Ismi: ')
#         surname = input('Familyasi: ')
#         email = input('Pochtasi: ')
#         age = input('Yoshi: ')
#         country = input('Davlati: ')
#
#         personal_data(name, surname, email, age, country)
#     else:
#         continue

# """ 3 """
#
# def kattasi(a, b, c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     elif c>a and c>b:
#         return c
#
# print(kattasi(3,5,1))

""" 4 """

# def aylana(R):
#     diametr = R*2
#     yuzi = 3.14*(R**2)
#     uzunligi = 2*3.14*R
#
#     aylana = {
#         'diametri': diametr,
#         'yuzi': yuzi,
#         'uzunligi': uzunligi
#     }
#     print(f'\n Ushbu {R} radiusli aylananing: ')
#     for i, j in aylana.items():
#         print(f'{i}:{j}')
#
# aylana(5)

""" 5 """

def interval_Tub(a,b):
    for i in range(a,b):
        k=0
        for j in range((i**1/2)//1):
            if i%j==0:
                k=k+1
