import random
#1.- Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print("Ejercicio 1")
def shuffle_list(lst):
    shuffled = lst[:] 
    random.shuffle(shuffled)  
    return shuffled

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffled_list = shuffle_list(my_list)
print(shuffled_list)

#2.- Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print("Ejercicio 2")
def unique_random_numbers():
    return random.sample(range(10), 7)  

print(unique_random_numbers())

print("revisado")