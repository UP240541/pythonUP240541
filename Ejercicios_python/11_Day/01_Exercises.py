#1.- Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print("Ejercicio 1")
def add_two_numbers():
    a = 2
    b = 4
    suma = a + b
    print("La suma es: ", suma)
add_two_numbers()    

#2.- Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
print("Ejercicio 2")
def AreaofCircle():
    pi = 3.141519
    radio = 5
    area = pi * radio * radio
    print("El area de un circulo es de: ", area)
AreaofCircle()

#3.- Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
print("Ejercicio 3")
def add_all_nums(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return sum(args)
    else:
        return "Error: Todos los elementos deben ser números."
print(add_all_nums(1, 2, 3, 4))  
print(add_all_nums(1, "a", 3)) 

#4.- Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
print("Ejercicio 4")
def CtoF():
    C = 39
    F = (C * 9/5) + 32
    print(C, "grados centigrados son: ", F)
CtoF()    

#5.- Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
print("Ejercicio 5")
Month = str(input("Ingrese un mes: "))
def checkSeason():
    if Month in ["Septiembre","Octubre", "Noviembre"]:
        print(Month, "esta en otoño")
    elif Month in ["Diciembre", "Enero", "Febrero"]:
        print(Month, "esta en invierno")
    elif Month in ["Marzo", "Abril", "Mayo"]:
        print(Month, "esta en primavera")
    elif Month in ["Junio", "Julio", "Agosto"]:
        print(Month, "esta en verano")
    else:
        print("Error") 
checkSeason()
#6.- Write a function called calculate_slope which return the slope of a linear equation
print("Ejercicio 6")
def calSlope(x1, y1, x2, y2 ):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calSlope(1, 2, 3, 6))

#7.- Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
print("Ejercicio 7")
import math
def solve_quadratic_eqn(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return (x1, x2)
    elif discriminante == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(abs(discriminante)) / (2 * a)
        return (complex(real_part, imag_part), complex(real_part, -imag_part))

print(solve_quadratic_eqn(1, -3, 2)) 
print(solve_quadratic_eqn(1, -2, 1)) 
print(solve_quadratic_eqn(1, 2, 5))

#8.- Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
print("Ejercicio 8")
def print_list(elements):
    for element in elements:
        print(element)
print_list([1, 2, 3, "ola", True])

#9.- Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print("Ejercicio 9")
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):  
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]

#10.- Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
print("Ejercicio 10")
def capitalize_list_items(items):
    return [item.capitalize() for item in items]

print(capitalize_list_items(["python", "java", "c++", "ruby"]))         

#11.- Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
print("Ejercicio 11")
def add_item(lst, item):
    lst.append(item)  
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))     # [2, 3, 7, 9, 5]

#12.- Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
print("Ejercicio 12")
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)  
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

#13.- Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print("Ejercicio 13")
def sum_of_numbers(n):
    return sum(range(1, n + 1))

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#14.- Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
print("Ejercicio 14")
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1, 2))

print(sum_of_odds(5))  
print(sum_of_odds(10)) 
print(sum_of_odds(1))
#15.- Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
print("Ejercicio 15")
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  
            total += i
    return total

print(sum_of_odds(5))   # 1 + 3 + 5 = 9
print(sum_of_odds(10))  # 1 + 3 + 5 + 7 + 9 = 25
print(sum_of_odds(1))