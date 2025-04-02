#1.- Write a function called is_prime, which checks if a number is prime.
print("Ejercicio 1")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(1))  
print(is_prime(4))  
print(is_prime(17)) 

#2.- Write a functions which checks if all items are unique in the list.
print("Ejercicio 2")
def unique(lst):
    return len(lst) == len(set(lst)) 

print(unique([1, 2, 3, 4]))  
print(unique([1, 2, 2, 4]))  
print(unique(["a", "b", "c"]))  
print(unique(["a", "b", "b"]))  

#3.- Write a function which checks if all the items of the list are of the same data type.
print("Ejercicio 3")
def sameType(lst):
    if not lst:  
        return True
    first_type = type(lst[0])  
    return all(type(item) == first_type for item in lst)

print(sameType([1, 2, 3, 4]))         
print(sameType([1, 2, "3", 4]))       
print(sameType(["a", "b", "c"]))      
print(sameType([1, 2.5, 3]))          

#4.- Write a function which check if provided variable is a valid python variable
print("Ejercicio 4")
import re

def validVariable(variable):
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable))

print(validVariable("my_var"))    
print(validVariable("myVar1"))    
print(validVariable("1myVar"))    
print(validVariable("_myVar"))    

#5- Go to the data folder and access the countries-data.py file.
print("Ejercicio 5")
import paises as p
datos = p.aaa

#6.- Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
idiomas = []
print("Ejercicio 6")

def most_spoken_languages():
    for pais in datos:
        for language in pais['languages']:
            idiomas.append(language)
    setLen = set(idiomas)
    dctLen = { }
    for language in setLen:
        dctLen[language] = 0
    for idioma in dctLen:
        for pais in datos:
            if idioma in pais ['languages']:
                dctLen[idioma] = pais['population'] + dctLen[idioma]
    sorValLenPop = sorted(dctLen.values(), reverse= True)                          
    sortKeyLenPop = sorted(dctLen,key=dctLen.get,reverse=True)
    return sortKeyLenPop[:10],sorValLenPop[:10]
print(most_spoken_languages())

#7.- Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
print("Ejercicio 7")
def most_populated_countries ():
    dctPop = {
    }
    for pais in datos:
        dctPop[pais['name']] = pais['population']
    sortValPop = sorted(dctPop.values(),reverse=True)
    sortKeyPop = sorted(dctPop,key=dctPop.get,reverse=True)
    return sortKeyPop[:10], sortValPop[:10]
print(most_populated_countries())