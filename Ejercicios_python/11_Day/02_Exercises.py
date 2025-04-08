#1.- Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
print("Ejercicio 1")
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = sum(1 for i in range(n + 1) if i % 2 != 0)
    return evens, odds
print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

#2.- Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
print("Ejercicio 2")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))  
print(factorial(0))  
print(factorial(1))  
print(factorial(7))  

#3.- Call your function is_empty, it takes a parameter and it checks if it is empty or not
print("Ejercicio 3")
def is_empty(value):
    return not bool(value)

print(is_empty(""))        
print(is_empty([]))        
print(is_empty({}))        
print(is_empty(None))      
print(is_empty(0))         
print(is_empty("Hola"))    
print(is_empty([1, 2, 3])) 
#4.-Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
print("Ejercicio 4")
from collections import Counter
import math
def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else None
def calculate_median(lst):
    if not lst:
        return None
    lst.sort()
    n = len(lst)
    mid = n // 2
    return (lst[mid] + lst[mid - 1]) / 2 if n % 2 == 0 else lst[mid]
def calculate_mode(lst):
    if not lst:
        return None
    freq = Counter(lst)
    max_count = max(freq.values())
    mode = [k for k, v in freq.items() if v == max_count]
    return mode[0] if len(mode) == 1 else mode
def calculate_range(lst):
    return max(lst) - min(lst) if lst else None

def calculate_variance(lst):
    if not lst or len(lst) < 2:
        return None
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / (len(lst) - 1)  

def calculate_std(lst):
    variance = calculate_variance(lst)
    return math.sqrt(variance) if variance is not None else None

data = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]

print("Mean:", calculate_mean(data))       
print("Median:", calculate_median(data))   
print("Mode:", calculate_mode(data))       
print("Range:", calculate_range(data))     
print("Variance:", calculate_variance(data))  
print("Std Dev:", calculate_std(data))     
print("revisado")