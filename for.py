# mehmonlar = ['Najmiddin', 'Lazizbek', 'Shahbos', 'Jahongir', 'Hasanboy', 'Muhammadyahyo']
# for mehmon in mehmonlar:
#     print(f"Hurmatli mehmon {mehmon} sizni 23-mart kuni to\'yga taklif etamiz")
#     print(f"Hurmat bilan Palonvhiyevlar oilasi \n")

# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2}")

# sonlar = list(range(1, 11))
# skvadrat = []
# for son in sonlar:
#     skvadrat.append(son**2)

# print(sonlar)
# print(skvadrat)

# dostlar = []
# print('5 ta eng yaqin do\'stingzni kiriting')
# for n in range(5):
#     dost = input(f"{n+1}-do'stingizni kiriting: ")
#     dostlar.append(dost.capitalize())
# print(dostlar)

# dostlar = ['ali', 'vali', 'islom', 'nur', 'yusuf']
# for n in dostlar:
#     print(f"Salom {n}")
# print(f"kod {len(n)} marta takrorlanadi")

# ninson = int(input("Bugun nechta odam bilan ko\'rishdingiz? "))
# ismlar = []
# for n in range(ninson):
#     ism = input(f"{n+1}-do'stingiz: ")
#     ismlar.append(ism.capitalize())
# print(ismlar)

# print("Beshta eng sevimli kiinolaringizni kiriting: ")
# kinolar = []
# for n in range(5):
#     kino = input(f"{n+1}-kino: ")
#     kinolar.append(kino.capitalize())
# print(f"kinolar ", kinolar)

# sonlar = list(range(10, 101))
# for n in sonlar:
#     print(n ** 3)


# Foydalanuvchidan 5 ta do‘sti ismini so‘rab, ularni ro‘yxatga saqlang. 
# So‘ng, har bir do‘st uchun "Salom, [ism]!" deb xabar chiqaring.
# print('5 ta do\'stingizni kiriting: ')
# dostlar = []
# for n in range(5):
#     ism = input(f"{n+1}-do'stingz: ")
#     dostlar.append(ism)
# for dost in dostlar:
#     print(f"Salom {dost.title()}")



# Foydalanuvchidan 3 ta sevimli raqamini so‘rab, ularni ro‘yxatga joylang. Keyin 
# har bir raqamni 2 barobar oshirib yangi ro‘yxat yarating va natijani ekranga chiqaring.
# print("3 ta raqam kiriting: ")
# raqamlar = []
# for n in range(3):
#     raqam = int(input(f"{n+1}-raqam: "))
#     raqamlar.append(raqam)

# nraqamlar = []
# for son in raqamlar:
#     nraqamlar.append(son * 2)

# print("Asl raqamlar: ", raqamlar)
# print("ko'paytma raqamlar: ", nraqamlar)



# Foydalanuvchidan 5 ta meva nomini kiritishini so‘rang. 
# So‘ng, har bir mevani bosh harfi katta bo‘lgan holda yangi ro‘yxatga saqlang va natijani ekranga chiqaring
# print("5 ta meva kiriting: ")
# mevalar = []
# for n in range(5):
#     meva = input(f"{n+1}-meva: ")
#     mevalar.append(meva.capitalize())
# print(mevalar)



# 1 dan 10 gacha bo‘lgan sonlarni ro‘yxatga joylang va har bir sonning kvadratini ekranga chiqaring.
# for son in list(range(10)):
#     print(son ** 2)



# Foydalanuvchidan 5 ta kitob nomini so‘rab, ularni ro‘yxatga saqlang. 
# So‘ng, ro‘yxatni teskari tartibda ekranga chiqaring.
print("5 ta kitob kiriting: ")
kitoblar = []
for n in range(5):
    kitob = input(f"{n+1}-kitob: ")
    kitoblar.append(kitob)
print(kitoblar, reverse=True)

