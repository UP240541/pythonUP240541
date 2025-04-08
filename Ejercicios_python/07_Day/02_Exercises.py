# Exercises: Level 2

#7 Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
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

print(A,B)
print("revisado")