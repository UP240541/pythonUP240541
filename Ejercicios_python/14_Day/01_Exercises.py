#1.- Explain the difference between map, filter, and reduce.
print("Ejercicio 1")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared) 
print("La clase 'map' aplica una funcion a cada funcion del iterable y devuelve un nuevo iterable con las funciones")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 
from functools import reduce
print("La clase filter filtra las iterables que cumplen con la condicion dada por la funcion")

product = reduce(lambda x, y: x * y, numbers)
print(product)
print("Aplica una funcion acumulativa a los elementos del iterable, reduciendolos a un unico valor")

#2.- Explain the difference between higher order function, closure and decorator
print("Ejercicio 2")
def apply_twice(func, x):
    return func(func(x))
def square(n):
    return n * n
result = apply_twice(square, 2)
print(result)
print("higher order function puede recibir otra función como argumento y devolver una función como resultado.")

def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply  
times3 = multiplier(3)  
print(times3(5))
print("Closure es una función anidada que recuerda las variables del ámbito en el que fue creada, incluso después de que ese ámbito haya finalizado")      

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
@debug
def add(a, b):
    return a + b
print(add(3, 4))
print("Un Decorator es una función especial que modifica el comportamiento de otra función sin alterar su código. Se suele usar con @decorator.")   

#3.-Define a call function before map, filter or reduce, see examples.
print("Ejercicio 3")
def call_before_map(call_func, map_func, iterable):
    processed_iterable = map(call_func, iterable)  
    return list(map(map_func, processed_iterable))  
def double(x):
    return x * 2  
def square(x):
    return x ** 2 
numbers = [1, 2, 3, 4]
result = call_before_map(double, square, numbers)
print(result)

#4.- Use for loop to print each country in the countries list.
print("Ejercicio 4")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

#5.- Use for to print each name in the names list.
print("Ejercicio 5")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)
          
#6.- Use for to print each number in the numbers list.
print("Ejercicio 6")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)