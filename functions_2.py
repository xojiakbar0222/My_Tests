# def print(a):
#     return a**2
#
# a=2
# print(print(a))

# """Funksiyadan lug'at qaytarish"""
# def person_info(name, surname, birth, gender, age, job = None):
#     "Insonlar haqida malumot berish funksiyasi"
#     person = {
#         'ism':name,
#         'familya':surname,
#         'tugilgan_yili':birth,
#         'jinsi':gender,
#         'yoshi':age,
#         'kasbi':job
#     }
#
#     return person
# odam_1 = person_info('Xojiakbar', 'Hasanov', 2001, 'male', 22, 'programmer')
# odam_2 = person_info('Muhammadjon', 'Hasanov', 2013, 'male', 9)
# people = [odam_2, odam_2]
#
# """2-usul"""
# print('Insonlar haqida malumotlar: ')
#
# for inson in people:
#     if inson['kasbi']:
#         job = person['kasbi']
#     else:
#         job = 'Nomalum'
#
#
# print(odam_1)
# print(odam_2)


def oila(n):
    oila = []
    for i in range (n):
        azo = input(f'{i+1} - oila azoingizning ismi :')
        oila.append(azo)
    return oila
oila1 = oila(4)
oila2 = oila(7)