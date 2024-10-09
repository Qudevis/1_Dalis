

# def kvadratu(skaicius : int) -> str:
#     print("Funkcija veikia")
#     return (skaicius ** 2) # 64

# rezultatas = kvadratu(8)


# def prideti_i_sarasa(sarasiukas): # dabar pasiimk sarasiukas (TAIP NEDAROM) # sarasiukas = 0x01
#     sarasiukas.append(10) # sarasiukas nebeegzistuoja

# sarasas = [7,89,1,2,6,8]
# sarasas2 = [3,9,2,1,5]
# sarasiukas = [8,3,1]

# prideti_i_sarasa(sarasas) # dabar imk sarasas (TAIP NEDAROM)

# prideti_i_sarasa(sarasas2)

# print(sarasas)

# print(sarasas2)

# print(sarasiukas)

# def spausdinti(sarasas):
#     print("Spausdinu grazia lentele su saraso duomenimis....")


# def suma(skaicius1, skaicius2):
#     suma = skaicius1 + skaicius2
#     return "Labas"

# print(suma(4,9))

# tuplius = (9,8,5)

# def prideti_i_tuple(tuplinis):
#     tuplinis.append(10)

# print(tuplius)

# def kvadratu(sk1):
#     return (sk1 ** 2) + 5

# kvadrats = lambda sk1: (sk1 ** 2 + 5)

# print(kvadrats(6))

# def atspausdink_su_veiksmu(funkcionalumas):
#     # iveskite su skaicius
#     # kvieciam funkcionaluma
#     print(funkcionalumas(9))

# atspausdink_su_veiksmu(kvadrats) # vietoje kvadrats sumuoti, dalinti, dauginti....


# sarasas = [1,2,3,4,5,6,7,8,9]

# kint = map(kvadratu,sarasas)
# kint = map(lambda sk1: (sk1 ** 2 + 5),sarasas)
# # naujas_sarasas = []
# # for sk in sarasas:
# #     naujas_sarasas.append(kvadrats(sk))

# print(list(kint))
# naujas_sarasas = []
# for sk in range(1,10):
#     if sk > 5:
#         naujas_sarasas.append(sk*sk)

# naujas_sarasas = [skaicius * skaicius for skaicius in range(1,10) if skaicius > 5] 

# print(naujas_sarasas)

# daugyba_is_saves = [lambda i=skaicius: i*i for skaicius in range(1,6)]
# for vienas in daugyba_is_saves:
#     print(vienas())

# def kvadratu(sk1):
#     print("As veikiu ir keliu kvadratu")
#     return (sk1 ** 2) + 5

# def atspausdink_su_veiksmu():
#     print("As veikiu ir meginu spausdinti")
#     return kvadratu # kvadratu(9) # 86

# print(atspausdink_su_veiksmu()(10))



# def get_adjacent_numbers(num: str): # ei kai naudosi mano funkcija nepamirsk kad cia turetu buti stringas
#     return [f"{i} - {str(i - 1)}{str(i + 1)}" for i in map(int, num)]
 
# user_input = input("Input: ")
# adjacent_numbers = get_adjacent_numbers(user_input)
# print(f"Output: {', '.join(adjacent_numbers)}")
 
# # f"{i} - {str(i - 1)}{str(i + 1)}"


# # [f"{i} - {str(i - 1)}{str(i + 1)}" for i in map(int, num)]

# # naujas = []

# # for i in map(int,user_input):
# #     naujas.append(f"{i} - {str(i - 1)}{str(i + 1)}")

# naujas = []

# for simbolis in user_input:
#     i = int(simbolis)
#     naujas.append(f"{i} - {i - 1} {i + 1}")

# print(f"mano tekstas: {user_input}")


# def suma_atimtis(skaicius, skaicius2):
#     suma = skaicius + skaicius2
#     skirtumas = skaicius-skaicius2
#     return suma, skirtumas


# atsakymas = suma_atimtis(9,5)
# print(atsakymas)
# print(atsakymas[1])
# suma, skirtumas = suma_atimtis(9,5)

# def viena_eilute(duotas_sarasas):
#     return list(map(lambda elementas:
#                      elementas[1]**duotas_sarasas[elementas[0]+1]
#                        if elementas[0] != len(duotas_sarasas)-1 else elementas[1]**2,
#                          enumerate(duotas_sarasas)))

# lst = [2, 5, 6, 8, 2]
# new_lst = []
 
# for i, val in enumerate(lst):
#     if i < len(lst)-1:
#         deg = lst[i+1]
#     else: deg = 2
 
#     new_lst.append(pow(val, deg))

# lst = [4,4,5,6,9,8,8,7,4,7,5]
# print(f"sarasas: {lst}")
# st = set(lst)

# print(st)

# naujas_st = {7,9,8,7,5}
# print(naujas_st)

# for i in naujas_st:
#     print(i)


# sarasas = ["Labas","Kaip","Sekasi"]

# print(" ".join(sarasas))







# def suma(test=15):
#     sumi = 5 + 9
#     print(sumi)
#     # return "Labas"

# print(suma(None)) # suma() -> "Labas"

# int(input(""))

# failas = open('testas.txt.txt','r')

# # tekstas = failas.read()
# # failas.seek(0)
# # tekstas2 = failas.read()


# zod = len(failas.read().split())
# sk = sum(char.isdigit() for char in failas.read())
# did = sum(char.isupper() for char in failas.read())
# maz = sum(char.islower() for char in failas.read())
 

# content = failas.read()

# zod = len(content.split())
# sk = sum(char.isdigit() for char in content)
# did = sum(char.isupper() for char in content)
# maz = sum(char.islower() for char in content)
# import time
# time.


# # importing the multiprocessing module
# import multiprocessing

# def print_cube(num):
#     """
#     function to print cube of given num
#     """
#     print("Cube: {}".format(num * num * num))

# def print_square(num):
#     """
#     function to print square of given num
#     """
#     print("Square: {}".format(num * num))

# if __name__ == "__main__":
#     # creating processes
#     p1 = multiprocessing.Process(target=print_square, args=(10, ))
#     p2 = multiprocessing.Process(target=print_cube, args=(10, ))

#     # starting process 1
#     p1.start()
#     # starting process 2
#     p2.start()

#     # wait until process 1 is finished
#     p1.join()
#     # wait until process 2 is finished
#     p2.join()

#     # both processes finished
#     print("Done!")

# import multiprocessing
# import time

# def pirma_uzduotis(num):
#     number = 1
#     for i in range(1, num):
#         if i % 2 == 0:
#             number = number * i
#         else:
#             number = number / i
#     print('pirma', number)


# def antra_uzduotis(num):
#     number = 1
#     for i in range(1, num):
#         if i % 2 == 0:
#             number = number * i
#         else:
#             number = number / i
#     print('antra', number)


# def trecia_uzduotis(num):
#     number = 1
#     for i in range(1, num):
#         if i % 2 == 0:
#             number = number * i
#         else:
#             number = number / i
#     print('trecia', number)


# if __name__ == '__main__':
#     multiprocessing.freeze_support()  

#     t1 = multiprocessing.Process(target=pirma_uzduotis, args=(60000000,))
#     t2 = multiprocessing.Process(target=antra_uzduotis, args=(60000000,))
#     t3 = multiprocessing.Process(target=trecia_uzduotis, args=(60000000,))
    
#     start_time = time.time()
    
#     t1.start()
#     t2.start()
#     t3.start()
    
#     t1.join()
#     print("Done! 1")
#     t2.join()
#     print("Done! 2")
#     t3.join()
#     print("Done! 3")
    
#     end_time = time.time()
#     print('Multiprocessing time:', f'{end_time - start_time:.2f} seconds')
    
#     start_time = time.time()
#     pirma_uzduotis(60000000)
#     antra_uzduotis(60000000)
#     trecia_uzduotis(60000000)
#     end_time = time.time()
#     print('Sequential execution time:', f'{end_time - start_time:.2f} seconds')

# pickle.dump([10,9,8,2,5], Failas) # pickle dump (arba pickle.write) (FAILAS = C:/Users/Justas/ManoAplankas)
# class Dog:
#     self.Name = "Reksas"
#     self.Age = 15

# # mano_suo = Dog("Reksas")
# pickle.dump(mano_suo,Failas)
# # FAILAS( Objektas Dog klases su reiksme name = "Reksas"  ir Age = 15                  )

# sunys = [Dog1, Dog2, Dog3]


# pickle.dump(sunys,Failas)
# # FAILAS( As turiu sarasa Objektu Dog klases su reiksme name = "Reksas"  ir Age = 15 name = "Margis"  Age 19...                 )


# uzkrauti_sunys = pickle.load(Failas)


# pickle.dump(biudzetas) (biudzetas zurnala turi dar kazka ir t.t )

# ukzrautas_biudzetas = pickle.load(Failas)

# uzkrautas_biudzetas.parodyti_ataskaita()

# Failas (Labas, kaip tau sekasi, man tai gerai, Valio, mums sekasi gerai)

# Failas.pickle (iojdgfoijdgifodgfdik)
import pickle 
# file = open("Failas.pickle","wb")
# pickle.dump("Sveiki", file)
# file.close()

# with open(r"Failas.pickle","wb") as file: # file = open("Failas.pickle","wb")
#     pickle.dump([7,4,5,3,8,5], file)
#     # file.close()

# with open(r"Failas.pickle","rb") as file: # file = open("Failas.pickle","wb")
#     nuskaitytas = pickle.load(file)
# nuskaitytas.append(19)
# print(nuskaitytas)
# sunys = []
# sunys.append(mano_suo)
# sunys.append(tavo_suo)
class Variklis():
    def __init__(self, title) -> None:
        self.title = title
        self.Testinis = "testuoju"

class Automobilis():
    def __init__(self, vardelis, age, engine) -> None: # vardelis = Reksas, age = 9 favFood = Maistas("Meat")
        self.Name = vardelis # self.Name = "Reksas"
        self.Age = age
        self.Engine = engine # FavouriteFood = Maistas("Meat")
    def __str__(self) -> str:
        return f"Gera masina vardu {self.Name}"
    def Lok(self):
        return "AU AU"
    
naujas_variklis = Variklis("1.9 Super Turbo")

mano_suo = Automobilis("Reksas",9,naujas_variklis)
tavo_suo = Automobilis("Margis",2, Variklis("Potato"))

sunys = [mano_suo,tavo_suo]
# with open(r"Failas.pickle","wb") as file: # file = open("Failas.pickle","wb")
#     pickle.dump(sunys, file) # buvo ir stringas ir sarasas ir t.t
#     # file.close()

# with open(r"Failas.pickle","rb") as file: # file = open("Failas.pickle","wb")
#     nuskaityti_automobiliai = pickle.load(file)
# print(nuskaityti_automobiliai[0].Engine.title)
# for suo in nuskaityti_automobiliai:
#     print(suo)

with open(r"Failas.pickle","ab+") as file: # file = open("Failas.pickle","wb")
    pickle.dump(sunys, file) # buvo ir stringas ir sarasas ir t.t
    file.seek(0)
    nuskaityti_automobiliai = pickle.load(file)
    for suo in nuskaityti_automobiliai:
        print(suo)

