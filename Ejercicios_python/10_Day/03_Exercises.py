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
fruit = ['banana', 'orange', 'mango', 'lemon']
reversa = []
for i in range(len(fruit) - 1, -1, -1):  
    reversa.append(fruit[i])

print(reversa)

#3.- Go to the data folder and use the countries_data.py file.
import countries-data as datos


#What are the total number of languages in the data

#Find the ten most spoken languages from the data

#ind the 10 most populated countries in the world