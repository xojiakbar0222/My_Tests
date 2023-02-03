"""15-dars"""

"""finally"""

"""
'try' blokida xatolik bolsa ham bolmasa ham, 'finally' ichidagi blok albatta ishlaydi

"""
# a = 'str'
# b = 10
#
# try:
#     print(a+b)
# except:
#     print("ERRor")
# else:
#     print('Finallyga ot')
# finally:
#     print('Salom') # Ushbu blok doim chop etiladi
#
# """Raise"""
# """xatolik vujudga kelganda foydalanuvchiga terminalda yuklatilgan izohni beradi"""

# a = 4
# b='ali'
#
# try:
#     print(a + b)
#
#     raise TypeError('Xatoli vujudga kelgandi, biz a ni matnga ogirib, keyin a ga b ni qoshdik')
# except TypeError:
#     a = str(a)
#     print(a+b)
#
# a = (input('Son kiriting: '))
# b = (input('2chi Sonni kiriting: '))
# try:
#     if int(a) > int(b):
#         print(a, ' katta ', b, ' dan')
#     elif int(a) == int(b):
#         print(a, ' teng ', b, ' ga ')
#     elif int(a) < int(b):
#         print(a, ' kichik ', b, ' dan')
#
# except ValueError:
#     print('siz kiritgan narsalardan kamida bittasi son emas')
# else:
#     print('Dasturizda hech qanday muammo yoq')

""" VAZIFA """

# """ 1 """
# numbers = [1, 2, 3, 8, 0, 0, 9, 9, 'anjir', 'anor']
# a = int(input('Son kiriting: '))
# i = 0
# for i in numbers:
#     try:
#         print(a/i)
#     except ZeroDivisionError:
#         i = 1
#         print('siz 0 raqamiga bolishga harakat qilgandiz, biz i ni 1 ga tenglab qoydik!!!')
#     except TypeError:
#         print('Siz Songa bolishiz kk edi')
#
#     except:
#         print('Bilganizni qiling!!!')



# """ 2 """
# def qoldiqsiz_bolnsin(a):
#     A = []
#     for i in range(1000):
#         try:
#             if i % a == 0:
#                 A.append(i)
#         except:
#             print('Muammosiz')
#     print(A)
#
# qoldiqsiz_bolnsin(int(input('a = ')))



""" 3 """

# try:
#     a = int(input('a = '))
#     b = int(input('b = '))
#     c = (a**2 + b**2)**(1/2)
# except ValueError:
#     print('son Qiymat kiritishingiz kerak')
#
# except:
#     print('Bilganizni qiling')

""" 4 """
fruit = ['banana', 'mandarin', 'apple', 'grape', 'cherry']
#fruit = 0
try:
    fruit = tuple(fruit)
    print(type(fruit))
    fruit = set(fruit)
    print(type(fruit))
except TypeError:
    print('fruit ni royxatga ozgartiring')

try:
    fruit.remove('shokolad')
    print(fruit)
# except  KeyError:
#     fruit.append('shokolad')
#     print('biz royxatingizda "shokolad" bolmagani uchun xafa bomasligiz uchun qoshib qoydik!!!', fruit)
#     fruit.remove('shokolad')
except KeyError or AttributeError:
    fruit = list(fruit)
    fruit.append('shokolad')
    print('biz royxatingizda "shokolad" bolmagani uchun xafa bomasligiz uchun qoshib qoydik!!!', fruit)
    fruit.remove('shokolad')




