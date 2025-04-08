#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
#Enter your age: 30
#You are old enough to learn to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.
print("Ejercicio 1")
age = int(input("Ingrese su edad: "))
if age > 17:
    print("Tienes la edad para conducir")
else:
    si = 18 - age
    print("Te faltan", si, "para aprender a conducir")

#2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences,
# and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
print("Ejercicio 2")
myAge = int(input("Ingrese su edad: "))
yourAge = int(input("Ingrese la edad de la otra persona: "))
if myAge > yourAge:
    print("Yo soy mayor")
    dif = myAge - yourAge
    if dif == 1:
        print("La diferencia de edad es de un año")
    else:
        print("Yo soy ", dif, " años mayor que tu")

elif yourAge > myAge:
    print("Tu eres mayor")    
    dif = yourAge - myAge
    if dif == 1:
        print("La diferencia de edad es de un año")
    else:
        print("Tu eres ", dif, " años mayor que yo")

elif myAge == yourAge:
    print("Tenemos la misma edad")


#3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
#  if a is less b return a is smaller than b, else a is equal to b. Output:
#Enter number one: 4
#Enter number two: 3
#4 is greater than 3
print("Ejercicio 3")
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un segundo numero: "))
if a > b:
    print(a," es mayor que ", b)
elif b > a:    
    print(b," es mayor que ", a)
elif a == b:
    print(a, " y ", b," son iguales")    

print("revisado")