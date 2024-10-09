# Šita kodo eilutė daro šį bei tą.....
# print("blabalbalbalba") # šito gali vėliau prireikti... Dėl to pasilieku neištrinu... ctrl + /
"""
dgfd
gdf """

# skaicius = 57465465
# suma = 5+9

# print(suma) 
# print(skaicius)
# print(skaicius)

# sk1 = 6
# sk2 = 2

# skirtumas = sk1 - sk2 # skirtumas = 6 - 2

# print(skirtumas)

# daugybos_rez = sk1 * sk2 + 3 - 5 + 1 - 8 /4 * 3

# print(daugybos_rez)

# trump = 9.87
# trump_suma = trump + 4.54
# print(trump)
# print(trump_suma)

# skaicius = 8
# skaicius2 = 3

# print(skaicius**skaicius2)

# print(skaicius // skaicius2)

# tekstas = "Tai yra labai geras tekstas man patinka rasyti tikiuosi patinka ir jums"

# print(tekstas)

# zodis = "labas"
# zodis2 = "kaip \t tau sekasi"

# print(zodis + " " + zodis2)


# tekstas = "hi Studentai megsta !@#$%^&*()* mokytis hi jiems patinka mokytis ir tikiuosi daug ismoks"

# print(tekstas[-2]) # minus tai nuo galo

# print(tekstas[0:2])
# print(tekstas[:30])

# print(tekstas[2])

# print(tekstas[::10])

# print(tekstas[::-2]) # po dveju dvitaskiu nurodytas skaicius nurodo kas kelinta raide spausdinti minusas nurodo kad is antro galo
# pakeistas_tekstas = tekstas[::-2]

# print(tekstas.upper().lower())

# vardas = "Saule"

# print("labas" + "kaip" + "tau sekasi" + vardas + " man tai gerai" + vardas)

# print(f"Labas, kaip tau {vardas} sekasi, man tai gerai {vardas}")

# amzius = 5
# tekstas = "Tavo amzius yra: "
# zodis = "15"

# print(tekstas + str(amzius))
# print(zodis + zodis)
# print(int(zodis) + float(zodis))

# print("-"*40)


# print("|"*40)
# print("-"*40)
# print(int("250")*4)

# print("zodis" + "zod")

# vardas = input("Iveskite savo varda: ")
# amzius = int(input("Iveskite savo amziu: ")) # "20"
# print(f"Sveiki, {vardas} {vardas}")

# print(f"Jusu amzius yra: {amzius+1}")

# if amzius > 20:
#     print("Tu gali nusipirkti alkoholio")
#     print("Be to labas")
#     if amzius > 65:
#         print("tu taip pat gauni pensija")
#         if amzius > 80:
#             print("tu jau ilgametis")
#     print("as esu pirmam ife")
#     print("as vis dar esu pirmam ife")

# print("Kaip tau sekasi")

# if amzius > 18:
#     print("Tu jau pilnametis")
# if amzius < 10:
#     print("Tu dar net ne paauglys")

# if amzius >= 18:
#     print("Tu jau pilnametis")
#     a = 15
#     suma = a + 19
# print(a)
# if amzius > 60:
#     print("tu jau senjoras")
# else:
#     print("Tu dar nesi senjoras")


# if amzius > 60 and amzius < 100:
#     print("Tu jau senjoras")
# elif amzius > 18 and amzius < 60:
#     print("tu jau pilnametis")
#     if amzius > 30 and amzius < 50:
#         print("Tu esi vidutinio amziaus")
#     elif amzius > 50:
#         print("hello")
# elif amzius > 100:
#     print("tu jau simtametis")
# else:
#     print("Tu vaikas")

# match amzius:
#     case skaicius if skaicius > 18 and skaicius < 60:
#         print("Tu pilnametis")
#     case 30: # elif amzius == 30
#         print("Tau lygiai trisdesimt")
#     case _:
#         print("Tu dar nesi suauges")


# match amzius:
#     case 15:
#         print("Tu pilnametis")
#     case 30: # elif amzius == 30
#         print("Tau lygiai trisdesimt")
#     case 45: # elif amzius == 45
#         print("Tau lygiai trisdesimt")
#     case 60: # elif amzius == 60
#         print("Tau lygiai trisdesimt")
#     case _:
#         print("Tu dar nesi suauges")


skaicius1 = float(input(" Iveskite skaiciu "))
skaicius2 = float(input(" Iveskite antra skaiciu "))

veiksmas = input("Iveskite norima veiksma (+,-,/,*)")



if veiksmas == '+':
    print(skaicius1 + skaicius2)
elif veiksmas == '-':
    print(skaicius1 - skaicius2)
elif veiksmas == '/':
    if skaicius2 == 0:
        print("Dalyba is nulio negalima")
    else:
        print(skaicius1 / skaicius2) # Cia dar nepatinka man...
elif veiksmas == '*':
    print(skaicius1 * skaicius2)
else:
    print("Ivedete kazka ne tokio")
