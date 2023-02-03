#masala

# A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b']
#
# ism_kiriting = str(input('Ismingizni kiriting: '))
# B = []
# a = list(ism_kiriting)
# print(list(a))
# b = 0
# for i in a:
#
#         b = A.index(i)
#         B.append(A[b-2])
#
# print(''.join(B))

alphabet = str(input('alfavitni kiriting: (probelsiz, ketma-ket!)'))
A = []
alphabet = list(alphabet)
print(alphabet)

ism_kiriting = str(input('Ismingizni kiriting: '))
B = []
length = int(input('matn nechtaga surilsin?: '))
a = list(ism_kiriting)
print(list(a))
b = 0
for i in a:

        b = A.index(i)
        B.append(A[b+length])

print(''.join(B))




