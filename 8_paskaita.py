# sarasas = [1,2,3,4,5,6]

# def kvadratu(x):
#     return x > 2


# lambda x: x > 2

# naujas = list(filter(lambda x: x > 2,sarasas))
# print(naujas)
# suma = 0
# for i in sarasas:
#     suma = suma * i

# from functools import reduce

# # a = 1; b = 2; a = a + b; b= 3; a+b (3+3)

# naujas = reduce(lambda a,b: a*b-1**2,sarasas)

# print(naujas)


# from statistics import median

sarasas = [4.5,1,7,9,5, 3] # [1 3 4 5 7 9]

# print(median(sarasas))

# naujas = [x*5 for x in sarasas if x > 3] #map(lambda x: x, sarasas)
# print(naujas)
# sarasas.append(50)
# print(naujas)

# print(type(5) is int)

# def sort(self) # self = sarasas
#         rikiuojam....
# NETURI RETURN

# sarasas.sort()
# print(sarasas)
# naujas = sorted(sarasas) # vietoje sorted sarasas atsistoja surikiuotas sarasas pvz [1,3,4.5,5,7,9]
# print(sorted(sarasas))

# print(sarasas)

# tuplas = (4.5,1,7,9,5, 3)

# naujas = sorted(tuplas)
# print(naujas)

# sort
# for in sarasas..
# tarpinis = sarasas[0]
# sarasas[0] = sarasas[1]
# sarasas[1] = tarpinis..

# Sorted
# naujas
# for in sarasas...
# naujas[0] = min(sarasas)
# naujas[1] = antras_min(sarasas)
# return naujas

# zodynas = {"Jonas":23,"Mantas":29,"Karolis":5,"Anzelmonas":87,"Benas":12}
# tuplai = sorted(zodynas.items())
# tuplai.append(("Benas",14))
# print(sorted(tuplai))

# zodynas = {"Jonas":23,"Mantas":29,"Karolis":5,"Anzelmonas":87,"Benas":12}
# sarasas_tuple = zodynas.items()
# print(sarasas_tuple)
# naujas = sorted(sarasas_tuple,key= lambda x: x[1])
# print(naujas)

# str - skirtas spausdinti vienam objektui pvz print(mano_automobilis)
# repr - skirtas spausdinti sarasui pvz print(automobiliai)

# class Car():
#     def __init__(self, make, model) -> None:
#         self.Make = make
#         self.Model = model
#     def __repr__(self) -> str:
#         return f"{self.Make} {self.Model}"

# automobiliai = [Car("Opel","Insignia"),Car("Audi", "S6"),Car("BWM", "X5"),
#                 Car("Volkswagen","Golf 7"),Car("Mazda","5"),Car("Toyota","Corolla"), Car("Toyota","Avensis")]

# def rikiavimas(automobilis : Car) -> str:
#     return automobilis.Make

# print(sorted(automobiliai, key=lambda aut: aut.Make))
# print(sorted(automobiliai, key=rikiavimas))

# from operator import attrgetter

# print(sorted(automobiliai, key=attrgetter("Make","Model")))



# x = 15



# def suma():
#     x = 20
#     return x

# print(suma())
# print(x)

# zip
vardai = ["Jonas","Mantas","Karolis", "Darius"]
pavardes = ["Jonaitis","Mantaitis", "Karolinis"]

print(dict(zip(pavardes,vardai)))

