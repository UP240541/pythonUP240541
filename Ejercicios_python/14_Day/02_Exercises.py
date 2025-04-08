#1.- Use map to create a new list by changing each country to uppercase in the countries list
print("Ejercicio 1")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
LstMapCoun = list(map(lambda x: x.upper(), countries))
print(LstMapCoun) 

#2.- Use map to create a new list by changing each number to its square in the numbers list
print("Ejercicio 2")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LstNumSqr = list(map(lambda x: x ** 2, numbers))
print(LstNumSqr)

#3.- Use map to change each name to uppercase in the names list
print("Ejercicio 3")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
LstNamUpp = list(map(lambda x: x.upper(), names))
print(LstNamUpp) 

#4.- Use filter to filter out countries containing 'land'.
print("Ejercicio 4")
def landin(country):
    if "land" in country:
        return True
    return False

inland = filter(landin, countries)
print(list(inland))  

#5.- Use filter to filter out countries having exactly six characters.
print("Ejercicio 5")
def sixcharcoun(country):
    if len(country) == 6:
        return True
    return False
countsix = filter(sixcharcoun, countries)
print(list(countsix))

#6.- Use filter to filter out countries containing six letters and more in the country list.
print("Ejercicio 6")
def sixlettcoun(country):
    if len(country) >= 6:
        return True
    return False
lettsixcount = filter(sixlettcoun, countries)
print(list(lettsixcount))

#7.- Use filter to filter out countries starting with an 'E'
print("Ejercicio 7")
def ecountry(country):
    if country[0:1] == 'E':
        return True
    return False
countre = filter(ecountry, countries)
print(list(countre))

#8.- Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print("Ejercicio 8")
numbers = [1, 2, 3, 4, 5, 6]
from functools import reduce
result = reduce(lambda x, y: x + y,filter(lambda x: x % 2 == 0,map(lambda x: x * 2,numbers)))
print(result)

#9.- Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
print("Ejercicio 9")
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
mixed_list = [1, 'hola', 3.14, 'adios', True, 'Yonaiker']
string_list = get_string_lists(mixed_list)
print(string_list)

#10.- Use reduce to sum all the numbers in the numbers list.
print("Ejercicio 10")
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)

#11.- Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print("Ejercicio 11")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ' and ' + countries[-1] + ' are north European countries.'

#12.- Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
print("Ejercicio 12")
from countries import countries  
def categorize_countries(pattern):
    return [country for country in countries if pattern in country]

land_countries = categorize_countries('land')
ia_countries = categorize_countries('ia')
island_countries = categorize_countries('island')
stan_countries = categorize_countries('stan')

print("Countries containing 'land':", land_countries)
print("Countries containing 'ia':", ia_countries)
print("Countries containing 'island':", island_countries)
print("Countries containing 'stan':", stan_countries)

#13.- Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
print("Ejercicio 13")
def count_countries_by_initial():
    country_dict = {}
    for country in countries:
        first_letter = country[0].upper()  
        country_dict[first_letter] = country_dict.get(first_letter, 0) + 1
    return country_dict

country_count_by_letter = count_countries_by_initial()
print(country_count_by_letter)

#14.- Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
print("Ejercicio 14")
def get_first_ten_countries():
    return countries[:10] 

first_ten = get_first_ten_countries()
print(first_ten)

#15.- Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print("Ejercicio 15")
def get_last_ten_countries():
    return countries[-10:] 

last_ten = get_last_ten_countries()
print(last_ten)

print("revisado")