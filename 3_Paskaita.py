# try:
# b = True
# b2 = False

# if b2:
#     print("Tikrai tiesa")
# ar_tiesa = 7==5

# if "dsada".isnumeric(): # True/False
#     print("Tiesa")

# sar = bool() # 0 - False | 1 - True
# print(not sar)
# if type(1) == int:
#     print("Tai tikrai skaicius")


# Paimkite šiandienos datą ir pasakykite, kokia data bus po 2 metų 4 mėnesių 27 dienų ir 16 valandų. 
 
# Gave šią datą atvaizduokite ją, ne standartinių formatu, pavyzdžiui, pirma mminutės po to metai ir t.t (formata galite pasirinkti patys, bet turi atsivaizduoti visos dalyks, tiek metai, tiek mėnesis tiek diena, tiek valandos (sekundės ir milisekundės nebūtina)

# import datetime as dt

# dob = dt.datetime(1999,7,5,15,34,20)

# # print(dob.strftime("%A,| %B")) # string from time

# pokytis = dt.timedelta(weeks=5)

# print((dob - pokytis))

# print(dt.datetime(day=10,year=2015,month=9))
# import dateutil
# import 1_dalis.1_Paskaita

# from dateutil.relativedelta import relativedelta as rd

# dob = dt.datetime(1999,1,28,15,34,20)

# dlt = rd(months=1)

# print((dob+dlt))

# import datetime as dt

# ivesta_data = input("Iveskite savo gimimo data ( tokiu formatu yyyy-mm-dd)")
# # strftime 
# data = dt.datetime.strptime(ivesta_data, "%Y-%m-%d %H")

# # print(data)
# # print(data.timestamp())
# # dt.datetime.fromtimestamp(936874800) # is timestamp (sekund )

# td = dt.timedelta(days=1)
# td_atimta = data - data
# print(((data +td) - data).total_seconds())


# try:
#     print("Dar nieko nezinau")
#     try:
#         7/0
#     except:
#         print("vidine dar klaida")
#     print("Viskas pavyko")
# except:
#     print("Klaida ivyko")

#     print("Labai baisi klaida")

# print("Hello as dar veikiu")

# except:
# Kazkur programoje ivyko klaida

try:
    # int("sadsa")
    7/0
    pass
except ZeroDivisionError:
    print("negalima dalinti is nulio")
    
except ValueError:
    print("Negalima konvertuoti stringo i skaiciu")
except:
    print("ivyko nezinoma klaida")
finally:
    print("viskas baigta")
    

print("Baigta po finally")
# try:
#     pass
# finally:
#     pass