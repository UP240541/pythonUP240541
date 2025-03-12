# Exercises: Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Find the length of the set it_companies
print(len(it_companies))

#2 Add 'Twitter' to it_companies
it_companies.add('Twatter')

#4 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Tencent','Meta','Intel'])
print(it_companies)

#5 Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

#6 What is the difference between remove and discard
print("Podemos remover items no especificados con discard(), en cambio remove() da error")
it_companies.pop()
print(it_companies)

# Exercises: Level 2

#7 Join A and B
AB = A.union(B) 
print(AB)

#8 Find A intersection B
print(A.intersection(B))

#9 Is A subset of B
print(A.issubset(B))

#10 Are A and B disjoint sets
print(A.isdisjoint(B))

#11 Join A with B and B with A
print(A.intersection(B))
print(B.intersection(A))

#12 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#13 Delete the sets completely
del A
del B

# Exercises: Level 3

#14 Convert the ages to a set and compare the length of the list and the
#  set, which one is bigger?
ageset = set(age)
print(len(age))
print(len(ageset))
if len(age) > len(ageset):
    print("La lista de edades es más grande")
else:
    print("El set de edades es más grande")

#15 Explain the difference between the following data types: string, list,
#  tuple and set
print("String es una secuencia de caracteres")
print("List son secuencias ordenadas de elementos")
print("Tuples son secuencias ordenadas de elementos inmutables")
print("Sets son elementos unicos desordenados")
#16 I am a teacher and I love to inspire and teach people.
#  How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
 
