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

print("revisado")
