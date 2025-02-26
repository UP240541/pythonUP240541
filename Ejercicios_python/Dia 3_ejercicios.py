#Dia 3 ejercicios
#1 Declare your age as integer variable
print("Ejercicio 1")
age = 18
print (age)
print (type(age))

#2 Declare your height as a float variable
print("Ejercicio 2")
height = 1.83
print (height)
print (type(height))

#3 Declare a variable that store a complex number
print("Ejercicio 3")
numeroComplex = 3+4j
print(numeroComplex)
numComp = complex(4,5)
print(numComp)

#4.- Write a script that prompts the user to enter base and height of the triangle 
# and calculate an area of this triangle (area = 0.5 x b x h).
print("Ejercicio 4")
base = float(input("Ingrese la base: "))
altura = float(input("Ingresa la altura: "))
area = (0.5 * base * altura)
print(area)

#5.-Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter 
# of the triangle (perimeter = a + b + c).
print("Ejercicio 5")
a = int(input("Ingresa el lado a: "))
b = int(input("Ingresa el lado b: "))
c = int(input("Ingresa el lado c: "))
per = (a+b+c)
print ("El perimetro del triangulo es: ", per)

#6.-Get length and width of a rectangle using prompt. Calculate its area (area = length x width) 
# and perimeter (perimeter = 2 x (length + width))
print("Ejercicio 6")
largo = int(input("Ingrese el largo del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))
area2 = (ancho * largo)
peri = (2 * (ancho + altura))
print("El area del rectangulo es de: ", area2, " El perimetro del rectangulo es de: ", peri)

#7.-Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print("Ejercicio 7")
pi = (3.14159)
rad = float(input("Ingrese el radio: "))
area3 = (pi * (rad * rad))
circum = (2 * pi * rad)
print ("El area del circulo es de: ", area3, " Y la circumferencia es de: ", circum)

#8.-Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("Ejercicio 8")
#trabajando en ello

#9.- Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
print("Ejercicio 9")
#trabajando en ello 

#10 Compare the slopes in tasks 8 and 9.
#print("Ejercicio 10")
#print("Comparar las pendientes de la 8 y 9")
#print(slope > slope2)
#print(slope < slope2)
#print(slope == slope2)
#print(slope >= slope2)
#print(slope <= slope2)
#print(slope != slope2)

#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print("Ejercicio 11")
x = float(input("Ingrese la cantidad: "))
y = x**2 + (6*x) + 9
if  y == 0:
    print("El valor de y es igual a 0")
else:
    print("El valor de y no es igual a 0")

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("Ejercicio 12")
print("12.-Encontrar la longitud de python y dragon, al final hacer un falso statement")
print("longitud de la palabra python: ")
print(len("python"))
print("Longitud de la palabra dragon: ")
print(len("dragon"))
print("¿Los dos tienen diferente longitud? ")
print(len('pyhton') != len('dragon')) 

#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("Ejercicio 13")
print('on in python', 'on' in 'python' and 'on in dragon', 'on' in 'dragon') 

#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("Ejercicio 14")
print('I hope this course is not full of jargon ', 'jargon' in 'I hope this course is not full of jargon')

#15 There is no 'on' in both dragon and python
print("Ejercicio 15")
print(not 'on' in 'python',not 'on' in 'dragon')

#16 Find the length of the text python and convert the value to float and convert it to string
print("Ejercicio 16")
length = (len("python"))
print(length)
print(type(length))
print(float(length))
print(type(float(length)))
print(str(length))
print(type(str(length)))

#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("Ejercicio 17")
numero = int(input("Ingresa un numero: "))
if numero % 2 == 0:
    print(numero, "es un numero par")
else:
    print(numero, "es un numero impar")

#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("Ejercicio 18")
num = 7 // 3
print(num)
conv = int(2.7)
if num == conv:
    print("Los numeros son iguales")
else:
    print("Los numeros no son equivalentes")
#19 Check if type of '10' is equal to type of 10
print("Ejercicio 19")
resultado = type('10') == type(10)
print(resultado)

#20 Check if int('9.8') is equal to 10
print("Ejercicio 20")
conv2 = int(9.8)
resultado2 = type('10') == type(10)
print(resultado2)
if conv2 == 10:
    print("Los numeros son iguales")
else:
    print("Los numeros no son iguales")
#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print("Ejercicio 21")
horas = int(input("Ingrese la cantidad de horas: "))
tarifa = int(input("Ingrese la tarifa por hora: "))
salario = horas * tarifa
print("Su salario semanal es de: ", salario)

#22 Write a script that prompts the user to enter number of years. Calculate the number of seconds
#  a person can live. Assume a person can live hundred years
print("Ejercicio 22")
anos = int(input("Ingrese una cantidad de años: "))
if anos > 100 and anos < 0:
    print("Valor invalido")
else:
    seg = anos * 31536
    print("Una persona de ", anos ," años vivio: ", seg ) 
#23 Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")