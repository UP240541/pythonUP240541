# Exercises: Level 2

#7 Join A and B
print("Ejercicio 7")
AB = A.union(B) 
print(AB)

#8 Find A intersection B
print("Ejercicio 8")
print(A.intersection(B))

#9 Is A subset of B
print("Ejercicio 9")
print(A.issubset(B))

#10 Are A and B disjoint sets
print("Ejercicio 10")
print(A.isdisjoint(B))

#11 Join A with B and B with A
print("Ejercicio 11")
print(A.intersection(B))
print(B.intersection(A))

#12 What is the symmetric difference between A and B
print("Ejercicio 12")
print(A.symmetric_difference(B))

#13 Delete the sets completely
print("Ejercicio 13")
del A
del B

# Exercises: Level 3

#14 Convert the ages to a set and compare the length of the list and the
#  set, which one is bigger?
print("Ejercicio 14")
ageset = set(age)
print(len(age))
print(len(ageset))
if len(age) > len(ageset):
    print("La lista de edades es más grande")
else:
    print("El set de edades es más grande")

#15 Explain the difference between the following data types: string, list,
#  tuple and set
print("Ejercicio 15")
print("String es una secuencia de caracteres")
print("List son secuencias ordenadas de elementos")
print("Tuples son secuencias ordenadas de elementos inmutables")
print("Sets son elementos unicos desordenados")
#16 I am a teacher and I love to inspire and teach people.
#  How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
print("Ejercicio 16") 
sent = ("I am a teacher and I love to inspire and teach people.")
dividido = sent.split()
print(len(dividido))