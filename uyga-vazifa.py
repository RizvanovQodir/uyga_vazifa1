# K va S hafrlari mavjud bolsa kattasini kichikka, kichigini kattaga ozgartiradi
# soz = "O'zbeKisTon"
# list1 = ['K','S']
# list2 = ['k','s']
# for i in soz:
#     if i in list1:
#         x = i.lower()
#     elif i in list2:
#         x = i.upper()
#     else:
#         x = i
#     print(x, end="")

# h = "#::##He,hhd###9$9" # stringlarni royhatga ajratadi
# x = h.split()
# print(x)

# a = h.strip('$')
# print(a)

# restoran = {
#     'osh' : {
#         "to'y osh" : 22000,
#         "choyxona osh" : 26000
#         },
#     'manti' : 5000,
#     'lagmon' : {
#         "suyuq lagmon" : 24000,
#         "qovurma lagmon" : 24000
#         },
#     'kabob' : 30000,
#     'norin' : 25000,
#     "sho'rva" : 22000,
#     'shashlik' : {
#         "qiyma" : 18000,
#         "jaz" : 20000
#     }
# }



# restoran = {
#     "taomlar" : {
#         "quyuq ovqatlar": {
#             "osh" : {
#                 "to'y osh" : 22000,
#                 "choyxona osh" : 26000
#             },
#             'manti' : 5000,
#             'lagmon' : {
#                 "suyuq lagmon" : 24000,
#                 "qovurma lagmon" : 24000
#             },
#             'kabob' : 30000,
#             'norin' : 25000,
#             'shashlik' : {
#                 "qiyma" : 18000,
#                 "jaz" : 20000
#             }
            
#         },
#         "suyuq ovqatlar" : {
#             "shorva" : {
#                 "qaynatma shorva" : 22000,
#                 "ko'za sho'rva" : 28000,
#             },
#             "mastava" : 24000,
#         }
#     },
# }

# mijoz = input("Assalomu alaykum Menyu bilan tanishasizmi? /ha yoki /yoq kabi belgilang:  ")

# if mijoz == '/ha':
#     for i in restoran["taomlar"].keys():
#         print(i)
#     taom = input("Nima buyurasiz: Suyuq /s, quyuq /q : ")
#     if taom == '/q':
#         for j in restoran["taomlar"]['quyuq ovqatlar'].keys():
#             print(j)
#         t = input("Biror taom tanlang: ")
#         for a ,b in restoran["taomlar"]['quyuq ovqatlar'].items():
#             if a == t:
#                 print(f"{a} ning narxi {b} som")
#             else:
#                 print(f"Mavjud taom: {a}")
#     elif taom == '/s':
#         for j in restoran["taomlar"]['suyuq ovqatlar'].keys():
#             print(j)
#         t = input("Biror taom tanlang: ")
#         for a ,b in restoran["taomlar"]['suyuq ovqatlar'].items():
#             if a == t:
#                 print(f"{a} ning narxi {b} som")
#             else:
#                 print(f"Mavjud taom: {a}")



br = input("Tugilgan vaqtingizni 1999-10-17 kabi kiriting: ")
br_year = int(br[:4])
br_month = int(br[5:7])
br_day = int(br[8:])

months = {
    '01' : 31,
    '02' : 28,
    '03' : 31,
    '04' : 30,
    '05' : 31,
    '06' : 30,
    '07' : 31,
    '08' : 31,
    '09' : 30,
    '10' : 31,
    '11' : 30,
    '12' : 31
}

months_kabisa = {
    '01' : 31,
    '02' : 29,
    '03' : 31,
    '04' : 30,
    '05' : 31,
    '06' : 30,
    '07' : 31,
    '08' : 31,
    '09' : 30,
    '10' : 31,
    '11' : 30,
    '12' : 31
}
s = 0
if br_year % 4 == 0 and br_year % 100 != 0 or br_year % 400 == 0:
    for i in months_kabisa.keys():
        if int(i) < br_month:
            s = s + months_kabisa[i]
    print(br_year, " boshidan beri", s + br_day, " kun vaqt o'tdi")
else:
    for i in months.keys():
        if int(i) < br_month:
            s = s + months[i]
    print(br_year, " boshidan beri", s + br_day, " kun vaqt o'tdi")
        
        
