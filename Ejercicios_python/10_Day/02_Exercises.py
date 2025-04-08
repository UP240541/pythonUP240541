#Exercises: Level 2
#1.- Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#The sum of all numbers is 5050.
print("Ejercicio 1")
suma = 0
for num in range(0, 101): 
    print(num)
    suma = suma + num
print("La suma de todos los numeros es: ",suma) 
#2.- se for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print("Ejercicio 2")
suma1 = 0
suma2 = 0
for num2 in range(0, 101):  
    if num2 % 2 == 0:  
        print(num2)
        suma1 = suma1 + num2  

for num3 in range(0, 101):  
    if num3 % 2 == 0:  
        pass
    else:
        print(num3)
        suma2 = suma2 + num3  
print("La suma de los valores par es: ", suma1, " Y la suma de los valos impar es: ", suma2)
#The sum of all evens is 2550. And the sum of all odds is 2500.

print("revisado")