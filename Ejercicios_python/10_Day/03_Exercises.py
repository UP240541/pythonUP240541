#Exercises: Level 3

#1.- Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
print("Ejercicio 1")
import countries as pis
paises = pis.countries
landCountries = []
for land in paises:
    if "land" in land: 
        landCountries.append(land)  

print("Países con 'land': ", landCountries)

#2.- This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print("Ejercicio 2")
fruit = ['banana', 'orange', 'mango', 'lemon']
reversa = []
for i in range(len(fruit) - 1, -1, -1):  
    reversa.append(fruit[i])

print(reversa)

#3.- Go to the data folder and use the countries_data.py file.
print("Ejercicio 3")
import paises as p
datos = p.aaa

#What are the total number of languages in the data
print("Ejercicio 3.1")
idiomas = []
for pais in datos:
    for lenguaje in pais['languages']:
        idiomas.append(lenguaje)        
        
print('lenguajes totales: ', len(idiomas))

#Find the ten most spoken languages from the data
print("Ejercicio 3.2")
setidiomas = set(idiomas)
dctidiomas = {}
for language in setidiomas:
    dctidiomas[language] = 0
for idioma in dctidiomas:
    for pais in datos:  
         if idioma in pais['languages']:
             dctidiomas[idioma] = pais['population'] + dctidiomas[idioma]
svLanguagePop = sorted(dctidiomas.values(), reverse= True)
skLanguagePop = sorted(dctidiomas, key= dctidiomas.get, reverse=True)
j = 0
for top in range(10):
    print( skLanguagePop[j], ": ",svLanguagePop[j])
    j+= 1

#rind the 10 most populated countries in the world
print("Ejercicio 3.3")
from paises import aaa 
ordenados = sorted(aaa, key=lambda item: item['population'], reverse=True)
print("Top 10 países más poblados:\n")
for pais in ordenados[:10]:
    print(pais['name'], pais['population'])

print("revisado")