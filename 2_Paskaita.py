# skaiciai = [4,5,1,2,25,-15]

# print(skaiciai)

# print(skaiciai[0]) # pasiimti elementa

# skaiciai[0] = 19 # pakeisti sarase esancio elemento reiksme

# print(skaiciai)

# print(skaiciai[0]) # pasiimti elementa

# trump_skaiciai = [4.9,5.1,1.3,2.5,25.8,-15.749]

# zodziai = ['Labas', "Kaip", 'Tau', 'Sekasi']

# # zodziai[2] = 'jam'

# # print(zodziai)

# print(skaiciai)
# skaiciai.append(50) #pridedame nauja skaiciu
# print(skaiciai)

# skaiciai2 = skaiciai.copy() # 0x0005

# skaiciai.append(33) # 0x0005 pridek 33
# skaiciai[0] = 22
# print(skaiciai)
# print(skaiciai2)


# skaiciai = [14,19,20,25,-15]

# print(skaiciai)
# skaicius = skaiciai.pop(0) # 14
# del skaiciai[0]
# skaiciai.remove(skaiciai[0])
# skaiciai.append(skaiciai)
# print(skaiciai)

# print(skaicius)

# kiekis = len(skaiciai)

# print(len(skaiciai))


# vidurkiai = {"Jonas": 9.87, "Marius":8.5,"Karolina":9.5}

# print(vidurkiai)

# print(vidurkiai["Karolina"])

# vidurkiai["Lukas"] = 8
# print(vidurkiai)

# vidurkiai["Marius"] = 9
# print(vidurkiai)
# vidurkiai.pop("Jonas")
# print(vidurkiai)


# skaiciai = [14,19,20,25,-15, "Hello"]
# suma = 0
# for skaicius in skaiciai: # 1 - iteracija skaicius = skaiciai[0] ... 2 - iteracija skaicius = skaiciai[1] ... 3 - iteracija skaicius = skaiciai[2]
#     if type(skaicius) == int: # 5 == 5
#         suma = suma + skaicius
#         suma += skaicius
# print(suma)
# averages = {"Jonas": 9.87, "Marius":8.5,"Karolina":9.5}



# # skaicius = 5
# # skaicius2 = 9

# # skaicius, skaicius2 = 5,9

# for key in averages: # eina per raktus # key = Jonas... key = Marius
#     print(key)

# for value in averages.values(): # eina per reiksmes
#     print(value)

# for kvp in averages.items(): # eina per raktu reiksmiu poras # 1. iteracija - kvp = ('Jonas', 9.87)
#     print(kvp)
# # name, average = Jonas, 9.87
# for name, average in averages.items(): # eina per raktu reiksmiu poras # 1. iteracija - kvp = ('Jonas', 9.87)
#     print(f"vardas: {name} vidurkis {average}")

# for kvp in averages.items(): 
#     name, average = kvp
#     print(f"vardas: {name} vidurkis {average}")

# studentai = {"Jonas":[7,9,7,5],"Mantas":[7,9,4,5],"Antanas":[7,9,1,9]}

# for vardas, pazymiai in studentai.items(): 
#     print(f"studentas {vardas} pazymiai {pazymiai} ")
# print(vardas)

# rng = list(range(10,101,5))
# print(rng)
# suma = 0
# for _ in range(3):
#     suma += int(input("iveskite skaiciu"))

# print(suma)

# a = 5

# while True:
#     a = a ** 2 # a = a + 5
#     print(a)

# sarase rasti 9 pozicija 
# ind = 0
# for skaicius in range(5,20,1):
#     if skaicius != 9:
#         ind += 1
#     else:
#         break
#     print(skaicius)
# print("indeksas yra: ",ind)

# while True:
#     if input("Iveskite kazka") == 'q':
#         break
#     else:
#         print("jus kazka ivedete")

# print("Baigiau")

# for skaicius in range(15,10):
#     print(skaicius)
# else:
#     print("Ciklas baigesi")

# a = 5

# while a < 100:
#     a = a + 5
#     print(a)
# else:
#     print("Baigiau while")

# for _ in range(2):
#     print(_)
    
#     for skaicius in range(15,20):
#         print(skaicius) 

# Tikslas: turime du sarasus ir reikia sukurti nauja sarasa kuris turetu tik elementus iš abieju sarasu
# pavizdys [4,89,2,4,85,54,8] kitas... [6,95,14,58,71,4,8] -> [4,8]

# sarasas = [4,9,6,5,14,1,6,65,65,4156]

# # print((19 in sarasas))

# if 9 in sarasas:
#     print("Radau")
# else:
#     print("Nera")

# arr1 = [1, 5, 9, 66, 33, 5]
# arr2 = [44, 6, 5,5, 66, 22, 1]
# arr3 = []
 
# for i in arr1:
#     if i in arr2 and i not in arr3:
#         arr3.append(i)
 
# print(arr3)

# Sugeneruokite žodyną su keliais žmonėmis (minimum 4) visi žmonės turėtų būti įvesti naudotojo. Žodynę turėtų būti žmogaus vardas ir jo pomėgiai/hobiai. Tikslas sukurti programą, kuri surastų kurie žmonės turi bendrus pomėgius ir kurie žmonės turi daugiausiai bendrų pomėgių (2 žmones), jeigu yra keli kurie turi vienodai pomėgių, grąžinti pagal eilę sąraše. 

# zodynas = {}

# for _ in range(3):
#     vardas = input("Iveskite varda: ")
#     pomegiai = []
#     for _ in range(2):
#         pomegiai.append(input("Iveskite pomegi: "))

#     zodynas[vardas] = pomegiai

# print(zodynas)

# zodynas = {'Jonas': ['Kasis', 'zvejyba'], 'Justas': ['Kasis', 'fule'], 'Karolis': ['begimas', 'ejimas']}
# poros = []
# for vardas, hobiai in zodynas.items():
#     for vardas2, hobiai2 in zodynas.items():
#         if vardas2 == vardas:
#             break
#         print(f"vardas su kuriuo lyginam 1 {vardas} vardas su kuriuo lyginam antras {vardas2}")
#         raktas = (vardas,vardas2)
#         pora = {raktas:[]}

#         for hobis in hobiai:
#             if hobis in hobiai2:
#                 poros[raktas]

#         poros.append(pora)
# print(poros)
    
# # list vs tuple Kuo jie skiriasi ?

# tup = (1,2,3)

# sarasas = [1,2,3]

# sarasas[0] = 5
# tup[0] = 5

# turesite du zodynus, isrinkite is siu zodynu sutampancius raktus (vardus) zodynai gali buti zmones su pazymiais ar dar kazkas..

# turekite pradini zodyna su 3 irasais, pasalinkite vidurini irasa (t.Y antra) ir idekite nauja irasa i zodyna viskas...

# Pameginkite sukurti sarasa (sakykime [4,8,9,5] svarbiausia daugiau nei pora elementu) ir pameginkite sukurti is jo nauja sarasa

# kuris butu atvirkscias [5,9,8,4] (ir ji atspausdinti)
# dic = {"test":1}
# print(dic["fgd"])


# # Original dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# # Desired key order
# new_order = ['c', 'a', 'b']

# # Reordered dictionary
# reordered_dict = {key: my_dict[key] for key in new_order}

# print(reordered_dict)



# zod = {1:10, 2:11.5, 3:12}
# zod = {1:"Jonas", "Mantas":"Petras", 3:"Antanas", 1: "Marius"}
# print(zod)


# first = {'Petras': 5, "Ieva": 8, "Marius": 9}
# second = {'Karolis': 8, 'Petras': 9, 'Robertas': 4, 'Marius': 9}
 
# for name in first:
#     if name in second.keys(): # zodyno_pavadinimas == zodyno_pavadinimas.keys()
#         print(name)
# Tekstas[2:5]
# sarasas = [4, 8, 9, 5]
# atvirkstinis = sarasas[::-1]
# print(atvirkstinis) 


# sarasas = [4,8,7,6,2,35,7,9]
# sarasas.reverse()
 
# print(sarasas) 


# class Animal():
#     def __init__(self, test : str) -> None:
#         self.test = test
#     def mazink(self):
#         return self.test.lower()

# class Dog(Animal):
#     def __init__(self, test : str) -> None:
#         # super().__init__(test)
#         self.testinis = test

# suo = Dog("HellO")
# suo.mazink()
# print()


if (5==7) | (6==6):
    print("Hello")