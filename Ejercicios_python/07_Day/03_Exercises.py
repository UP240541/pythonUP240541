# Exercises: Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]
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
print(len(sent))
dividido = sent.split()
print(len(dividido))

print("revisado") #No se ejecuta // Arreglado