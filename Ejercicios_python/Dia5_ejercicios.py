#Iniciando 
#1 Declare an empty list
print("Ejercicio 1")
mtlist = list()
#2 Declare a list with more than 5 items
print("Ejercicio 2")
cositas = ['cosa1', 'cosa2', 'cosa3', 'cosa4', 'cosa5']
print(cositas)

#3 Find the length of your list
print("Ejercicio 3")
print(len(cositas))

#4 Get the first item, the middle item and the last item of the list
print("Ejercicio 4")
cosa1 = cositas[0]
cosamed = cositas[2]
cosalast = cositas[4]
print(cosa1, cosamed, cosalast)

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
print("Ejercicio 5")
mixDataTypes = ['Yonaiker', '69', '1.5', 'married', 'Venezuela york']

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print("Ejercicio 6")
itCompanies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7 Print the list using print()
print("Ejercicio 7")
print(itCompanies)

#8 Print the number of companies in the list
print("Ejercicio 8")
print(len(itCompanies))

#9 Print the first, middle and last company
print("Ejercicio 9")
cfirst = itCompanies[0]
cmid = itCompanies[3]
clast = itCompanies[6]
print(cfirst, cmid, clast)

#10 Print the list after modifying one of the companies
print("Ejercicio 10")
itCompanies[0] = 'Meta'
print(itCompanies) 

#11 Add an IT company to it_companies
print("Ejercicio 11")
itCompanies.append('pillofon')
print(itCompanies)
#12 Insert an IT company in the middle of the companies list
print("Ejercicio 12")
itCompanies.insert(4, 'tencent')
print(itCompanies)
#13 Change one of the it_companies names to uppercase (IBM excluded!)
print("Ejercicio 13")
print(itCompanies[0].upper())

#14 Join the it_companies with a string '#;  '
print("Ejercicio 14")
unido = "#; ".join(itCompanies)
print(unido)


#15 Check if a certain company exists in the it_companies list.
print("Ejercicio 15")
siExiste = 'Amazon' in itCompanies
print(siExiste) 

#16 Sort the list using sort() method
print("Ejercicio 16")
itCompanies.sort()
print(itCompanies)

#17 Reverse the list in descending order using reverse() method
print("Ejercicio 17")
itCompanies.sort(reverse=True)
print(itCompanies)

#18 Slice out the first 3 companies from the list
print("Ejercicio 18")
print(itCompanies)
firstThree = itCompanies[3:]
print(firstThree)
#19 Slice out the last 3 companies from the list
print("Ejercicio 19")
lastThree = itCompanies[0:6]
print(lastThree)

#20 Slice out the middle IT company or companies from the list
print("Ejercicio 20")
midslice = itCompanies[0:4],itCompanies[5:] 
print(midslice)
#21 Remove the first IT company from the list
print("Ejercicio 21")
itCompanies.pop(0)
print(itCompanies) 

#22 Remove the middle IT company or companies from the list
print("Ejercicio 22")
itCompanies.remove('Meta')
itCompanies.remove('IBM')
print(itCompanies) 

#23 Remove the last IT company from the list
print("Ejercicio 23")
itCompanies.pop()
print(itCompanies) 

#24 Remove all IT companies from the list
print("Ejercicio 24")
itCompanies.clear
print(itCompanies)

#25 Destroy the IT companies list
print("Ejercicio 25")
del(itCompanies)

#26 Join the following lists:
print("Ejercicio 26")
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
allEnd = front_end + back_end
print(allEnd)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
print("Ejercicio 27")
full_stack = allEnd.copy()
print(full_stack)
full_stack.insert(8, 'Python')   
full_stack.insert(9, 'SQL')
print(full_stack) 

#Exercises: Level 2
#The following is a list of 10 students ages:
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#28 Sort the list and find the min and max age
print("Ejercicio 28")
ages.sort()
print(ages)
minage = ages[0] 
print(minage)      
last_index = len(ages) - 1
maxage = ages[last_index]
print(maxage)

#29 Add the min age and the max age again to the list
print("Ejercicio 29")
ages.append(19)    
ages.append(26)
ages.sort()
print(ages)

#30 Find the median age (one middle item or two middle items divided by two)  
print("Ejercicio 30")
firstMiddle = ages[5]
secondMiddle = ages[6]


#31 Find the average age (sum of all items divided by their number )
print("Ejercicio 31")
print(len(ages))
avrg = (19 + 22 + 19 + 24 + 20 + 25 + 26 + 24 + 25 + 24) / len(ages)
print(avrg)

#32 Find the range of the ages (max minus min)
print("Ejercicio 32")
rango = 26 - 19
print(rango)

#33 Compare the value of (min - average) and (max - average), use abs() method
print("Ejercicio 33")

diffMin = abs(minage - avrg)
diffMax = abs(maxage - avrg)
print(diffMax)
print(diffMin)
if diffMin > diffMax:
    print("La diferencia mínima es mayor")
else:
    print("La diferencia máxima es mayor")

#34 Find the middle country(ies) in the countries list
print("Ejercicio 34")
import countries as pis
paises = pis.countries
print(len(pis.countries))
medio = len(pis.countries) // 2  
print(medio)
paisMedio = pis.countries[medio]  
print(paisMedio)

#35 Divide the countries list into two equal lists if it is even if not one more country for the first half.
print("Ejercicio 35")
firstHalf = pis.countries[0:97]
print(len(firstHalf))
secondHalf = pis.countries[97:]
print(len(secondHalf))

#36 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = countries2
print(ch)
print(ru)
print(us)
print(scandic)
