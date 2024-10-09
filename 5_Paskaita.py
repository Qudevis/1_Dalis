# class Dog: # Klase Dog - kuri yra kaip sablonas
#     def __init__(self,spalva, legs=4): # Konstruktorius, kuris inicilizuoja objekta ir nurodo jo pradinius dalykus
#         self.__color = spalva # private self.color
#         self.pazymiai = [7,9,8,5,2]
#         self.kojos = legs
#         print("Sukiuriau suni")
    
#     def Lok(self):
#         print("AU AU")

#     def pakeisk_spalva(self, spalva):
#         if spalva == "Balta":
#             print("Spalva netinkama")
#         else:
#             self.__color = spalva

#     def __patikrinimas(self):
#         pass

#     def patikrinimas(self):
#         pass

#     def grazink_spalva(self):
#         self.__patikrinimas()
#         if self.__color == "Juoda":
#             return self.__color
#         else:
#             return "Neteisinga spalva"

#     def __apibudink(self):
#         print(f"Labas, as esu {self.__color} suo")

#     def apibudink(self):
#         self.__patikrinimas()
#         print(f"Labas, as esu {self.__color} suo")
#     # def return_color(self):
#     #     return self.color

# mano_suo = Dog("Juodas",3) # Dog.__init__("Juodas")
# tavo_suo = Dog("Rudas") # tavo suo yra objektas, tai yra pagal sablona (klase) sukurtas kintamasis
# tavo_suo.apibudink()
# mano_suo.__naujas = 9
# print(mano_suo.__naujas)
# print(mano_suo._Dog__color) # self.color
# # print(tavo_suo.color)
# mano_suo.Lok()
int("-5")
class Dog: # Klase Dog - kuri yra kaip sablonas
    def __init__(self,spalva : str, legs=4): # Konstruktorius, kuris inicilizuoja objekta ir nurodo jo pradinius dalykus
        self.color = spalva # private self.color
        self.kojos = legs
    
    def Lok(self):
        print("AU AU")
    
    def apibudink(self) -> str:
        return f"Labas as esu suo su {self.kojos} kojomis ir esu {self.color} spalvos"
    
    def __str__(self) -> str:
        return f"Labas as esu suo su {self.kojos} kojomis ir esu {self.color} spalvos"
    
    def __repr__(self) -> str:
        return f"Geras suo {self.color} spalvos"

reksas = Dog("Brown")
lese = Dog("White")
reksas.apibudink()
# print(reksas.apibudink())
# # print(reksas)
# # print(lese.kojos)

# def apibudink(suo) -> str:
#     return f"Labas as esu suo su {suo.kojos} kojomis ir esu {suo.color} spalvos"

# rezultatas = apibudink(reksas) # rezultatas = f"Labas as esu suo su {suo.kojos} kojomis ir esu {suo.color} spalvos"

# print(rezultatas)
# tina = Dog("Yellow",3)
# dogs = [reksas,lese,tina]
# print(dogs)
# for dog in dogs:
#     dog.color = "Juoda"
#     print(dog)

# print(dogs)


# for i in range(50):
#     print(i)
