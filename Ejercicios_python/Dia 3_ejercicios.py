#Dia 3 ejercicios
#1
age = 18
print (age)
print (type(age))

#2
height = 1.83
print (height)
print (type(height))

#3
numeroComplex = 2643.575
print(numeroComplex)
print(type(numeroComplex))

#4.- Write a script that prompts the user to enter base and height of the triangle 
# and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Ingrese la base: "))
altura = float(input("Ingresa la altura: "))
area = (0.5 * base * altura)
print(area)

#5.-Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter 
# of the triangle (perimeter = a + b + c).
a = int(input("Ingresa el lado a: "))
b = int(input("Ingresa el lado b: "))
c = int(input("Ingresa el lado c: "))
per = (a+b+c)
print ("El perimetro del triangulo es: ", per)

#6.-Get length and width of a rectangle using prompt. Calculate its area (area = length x width) 
# and perimeter (perimeter = 2 x (length + width))
largo = int(input("Ingrese el largo del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))
area2 = (ancho * largo)
peri = (2 * (ancho + altura))
print("El area del rectangulo es de: ", area2, " El perimetro del rectangulo es de: ", peri)

#7.-Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = (3.14159)
rad = float(input("Ingrese el radio: "))
area3 = (pi * (rad * rad))
circum = (2 * pi * rad)
print ("El area del circulo es de: ", area3, " Y la circumferencia es de: ", circum)

#8.-Calculate the slope, x-intercept and y-intercept of y = 2x -2