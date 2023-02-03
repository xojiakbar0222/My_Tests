"""Arifmetik amallar"""

"""
x*=y   x ni y ga kopaytirib, natijani x ga qayta ozlashtiradi x = x * y
x/=y   x ni y ga bolib, qiymatni x ga ozlashtiradi            x = x / y
x**=y  darajaga kotarib, x ga ozlashtiradi                    x = x ** y
x//=y yaxlidlab bolib, x ga ozlashtiradi                      x = x // y
x%=y qoldiqli bolib, x ga ozlashtirib qoyadi                  x = x % y
"""
"""
x=5
and ikki shart togri bolsa x>2 and x<10
or 
# """
# A = [1, 2,3]
#
# if 1 not in A:
#     print('Hello')
# else:
#     print('yes')

a = 5
b = -6
print('a+b = ', a + b)
print('a-b = ', a - b)
print('a//b = ', a // b)
print('a%b = ', a % b)
a += b
print('a+=b ==> ', a)
a -= b
print('a-=b ==> ', a)
a *= b
print('a*=b ==> ', a)
a /= b
print('a/=b', a)
a %= b
print('a%=b ==>', a)
a //= b
print('a//=b ==> ', a)

print('a != b ==> ', a != b)
print('a > b ==> ', a > b)
print('a < b ==> ', a < b)
print('a is b ==> ', a is b)
print('a is not b ==> ', a is not b)

A = [1, 2, 3]

print('1 in A ==> ', 1 in A)
print('4 not in A', 4 not in A)
print('A[0] is not str ==> ', A[0] is not str)

