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
print('Complex number: ', 1 + 1j)


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
def line_properties(equation):
    # Parse the equation of the form y = mx + b
    equation = equation.replace("y =", "").strip()
    m, b = equation.split("x")
    m = float(m.strip())
    b = float(b.strip())

    # Calculate slope, x-intercept, and y-intercept
    slope = m
    x_intercept = -b / m
    y_intercept = b

    return slope, x_intercept, y_intercept


equation = "y = 2x -2"
slope, x_intercept, y_intercept = line_properties(equation)

print(f"Equation: {equation}")
print(f"Slope: {slope}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

#9.- Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
def calculate_slope_and_distance(x1, y1, x2, y2):
    # Calculate slope
    slope2 = (y2 - y1) / (x2 - x1)
    import math
    # Calculate Euclidean distance
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return slope2, distance
# Points
x1, y1 = 2, 2
x2, y2 = 6, 10
# Compute results
slope2, distance = calculate_slope_and_distance(x1, y1, x2, y2)
# Output results
print(f"Points: ({x1}, {y1}), ({x2}, {y2})")
print(f"Slope: {slope2}")
print(f"Euclidean Distance: {distance}")

#10 Compare the slopes in tasks 8 and 9.
print("Comparar las pendientes de la 8 y 9")
print(slope > slope2)
print(slope < slope2)
print(slope == slope2)
print(slope >= slope2)
print(slope <= slope2)
print(slope != slope2)
#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print("12.-Encontrar la longitud de python y dragon, al final hacer un falso statement")
print("longitud de la palabra python: ")
print(len("python"))
print("Longitud de la palabra dragon: ")
print(len("dragon"))
print("¿Los dos tienen diferente longitud? ")
print(len('pyhton') != len('dragon')) 
#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on in python', 'on' in 'python' and 'on in dragon', 'on' in 'dragon') 
#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('I hope this course is not full of jargon ', 'jargon' in 'I hope this course is not full of jargon')
#15 There is no 'on' in both dragon and python
print(not 'on' in 'python',not 'on' in 'dragon')
#16 Find the length of the text python and convert the value to float and convert it to string
length = (len("python"))
print(length)
print(type(length))
print(float(length))
print(type(float(length)))
print(str(length))
print(type(str(length)))

#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numero = (input("Ingresa un numero: "))

#18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

#19 Check if type of '10' is equal to type of 10

#20 Check if int('9.8') is equal to 10

#21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

#22

#23

#24 