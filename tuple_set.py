""" TUPLE """

# meva = ('apple', 'dfdf')
# print(type(meva))
#
# meva = ('apple') #tuple emas, bolishi uchun 2 va undan ortiq elementdan iborat bolishi kk
#
# #ikkita tupleni bir-biriga qoshsa boladi, lekin bitta tuple ga dan element qoshib yoki ayrib tashlolmaymiz
# tuple1 = ('a', 'b', 'c')
# tuple2 = (1, 2, 3)
# tuple = tuple2 + tuple1
# print(tuple)

""" set """
''' Set tartibsiz, ozgarmas va indekslanmagan toplamdir is 
Set elementlari ozgartirish mumkin emas, lekin elementlari olib tashlash va yangi element qoshish mumkin.
set tartibsiz'''

"""elementlar .add metodi orqali qoshiladi"""
"""elementlar .remove()(yoq narsaga xatolik beradi, discard()(bu esa bermaYdi"""

'''ikkita setni qoshish .update() va union.() metodlari orqali amalga oshiriladi
 name3 = '''
# set(tuple1)
# set(tuple2)
# tuple = tuple2 + tuple1
# print(tuple)
# print(tuple)

"""Vazifa - Tuple"""

# # """1"""
# family = ('dadam', 'ayam', 'akam', 'ukam')
# print('oilamda: \n', family, ' bor!')
#
# #
# '''1.1'''
# family = list(family)
# a = family.pop(2)
# b = family.pop(2)
# print('\noilamda \n',family,' qolishdi!' )
#
# """1.2"""
# family[0] += ' - Bahodirjon'
# family[1] += ' - Umarova'
#
# print(family)
# #
# # """1.3"""
# # family.append(a)
# # family.append(b)
# # print(family)


# """2"""
# positive_numbers = [1, 2, 3, 4, 5]
# negative_numbers = [-1, -2, -3, -4]
# all_numbers = []
# all_numbers.append(positive_numbers)
# all_numbers.append(negative_numbers)
# all_numbers_2 = tuple(all_numbers)
# print(type(all_numbers_2))
# print(all_numbers_2)
# del all_numbers_2
# print(all_numbers_2)

# """3"""
# names = ['anvar', 'akmal', 'zebo']
# numbers = (1, 2, 3, 4)
# """3.1"""
# names = set(names)
# numbers = set(numbers)
# total = names.union(numbers)
# print(type(total))
# print(total)

# """3.2"""
# names = tuple(names)
# total = names + numbers
# total = set(total)
# print(type(total))
# print(total)



# """4"""
#
# fruit = ['apple', 'banana', 'grape', 'orange', 'strawberry', 'cherry', 'mandarin']
# print(fruit, type(fruit))
# fruit = tuple(fruit)
# print(fruit, type(fruit))
# fruit = set(fruit)
# print(fruit, type(fruit))
#
# """4.1"""
# fruit.remove('apple')
# fruit.discard('grape')
# #fruit.remove('olma')#xatolik beradi
# fruit.discard('olma')
# #fruit.remove('anor')
# fruit.discard('anor')
# print(fruit)
#
# fruit.add('kivi')
# fruit.add('kakos')
# fruit.add('anjir')
#
# print(fruit)
#
# print(fruit.clear())
# print(fruit)
# del fruit

# '''5'''
# positive_numbers = [1, 2, 3, 4, 5]
# negative_numbers = [-1, -2, -3, -4]
# positive_numbers = set(positive_numbers)
# negative_numbers = set(negative_numbers)
# all_numbers = positive_numbers.union(negative_numbers)
# positive_numbers.update(all_numbers)
# negative_numbers.update(all_numbers)
# print(all_numbers)
# print(positive_numbers)
# print(negative_numbers)




