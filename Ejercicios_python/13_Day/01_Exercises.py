#1.- Filter only negative and zero in the list using list comprehension
print("Ejercicio 1")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negNum = [i for i in numbers if i < 1 ]

print(negNum)

#2.- Flatten the following list of lists of lists to a one dimensional list :
print("Ejercicio 2")
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for row1 in list_of_lists for row2 in row1 for number in row2]
print(flattened_list)
#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#3.- Using list comprehension create the following list of tuples:
print("Ejercicio 3")
renglon1 = [(i, 1, i,  i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11) ]
#numbers = [(i, i * i) for i in range(11)]
#print(numbers)  
print(renglon1)   
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

#4.- Flatten the following list to a new list:
print("Ejercicio 4")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list2 = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]
print(flattened_list2)
#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

#5.- Change the following list to a list of dictionaries:
print("Ejercicio 5")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lstTodct = [{'country':country.upper(), 'city':capital.upper()} for sublist in countries for country, capital in sublist]
print(lstTodct)
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

#6.- Change the following list of lists to a list of concatenated strings:
print("Ejercicio 6")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for sublist in names for name in sublist]

print(concatenated_names)
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

#7.-Write a lambda function which can solve a slope or y-intercept of linear functions.
print("Ejercicio 7")
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x1 != x2 else None

print(slope(1, 2, 3, 6))
