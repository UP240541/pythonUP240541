#Iniciando 
#1 Declare an empty list
mtlist = list()
#2 Declare a list with more than 5 items
cositas = ['cosa1', 'cosa2', 'cosa3', 'cosa4', 'cosa5']
print(cositas)

#3 Find the length of your list
print(len(cositas))

#4 Get the first item, the middle item and the last item of the list
cosa1 = cositas[0]
cosamed = cositas[2]
cosalast = cositas[4]
print(cosa1, cosamed, cosalast)

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixDataTypes = ['Yonaiker', '69', '1.5', 'married', 'Venezuela york']

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
itCompanies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7 Print the list using print()
print(itCompanies)

#8 Print the number of companies in the list
print(len(itCompanies))

#9 Print the first, middle and last company
cfirst = itCompanies[0]
cmid = itCompanies[3]
clast = itCompanies[6]
print(cfirst, cmid, clast)

#10 Print the list after modifying one of the companies
itCompanies[0] = 'Meta'
print(itCompanies) 

#11 Add an IT company to it_companies
itCompanies.append('pillofon')
print(itCompanies)
#12 Insert an IT company in the middle of the companies list
itCompanies.insert(4, 'tencent')
print(itCompanies)
#13 Change one of the it_companies names to uppercase (IBM excluded!)
print(itCompanies[0].upper())

#14 Join the it_companies with a string '#;  '
unido = "#; ".join(itCompanies)
print(unido)


#15 Check if a certain company exists in the it_companies list.
siExiste = 'Amazon' in itCompanies
print(siExiste) 

#16 Sort the list using sort() method
itCompanies.sort()
print(itCompanies)

#17 Reverse the list in descending order using reverse() method
itCompanies.sort(reverse=True)
print(itCompanies)

#18 Slice out the first 3 companies from the list
print(itCompanies)
firstThree = itCompanies[3:]
print(firstThree)
#19 Slice out the last 3 companies from the list
lastThree = itCompanies[0:6]
print(lastThree)

#20 Slice out the middle IT company or companies from the list
midslice = itCompanies[0:4],itCompanies[5:] 
print(midslice)
#21 Remove the first IT company from the list
itCompanies.pop(0)
print(itCompanies) 

#22 Remove the middle IT company or companies from the list
itCompanies.remove('Meta')
itCompanies.remove('IBM')
print(itCompanies) 

#23 Remove the last IT company from the list
itCompanies.pop()
print(itCompanies) 

#24 Remove all IT companies from the list
itCompanies.clear
print(itCompanies)

#25 Destroy the IT companies list
del(itCompanies)

#26 Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
allEnd = front_end + back_end
print(allEnd)

#27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.


#Exercises: Level 2

#The following is a list of 10 students ages:
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#28 Sort the list and find the min and max age
#29 Add the min age and the max age again to the list
#30 Find the median age (one middle item or two middle items divided by two)
#31 Find the average age (sum of all items divided by their number )
#32 Find the range of the ages (max minus min)
#33 Compare the value of (min - average) and (max - average), use abs() method
#34 Find the middle country(ies) in the countries list
#35 Divide the countries list into two equal lists if it is even if not one more country for the first half.
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
