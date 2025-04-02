#1.- Write a function which generates a six digit/character random_user_id.
import random
import string
print("Ejercicio 1")        
def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))   
print(random_user_id())
#'1ee33d'

#2.- Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print("Ejercicio 2")        
def user_id_gen_by_user():
    char = int(input("Ingrese el numero de caracteres id: "))
    num = int(input("Ingrese el numero de IDs que se generaran: "))
    ids = [''.join(random.choices(string.ascii_letters + string.digits, k=char)) for _ in range(num)]
    for user_id in ids:
        print(user_id)

print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

#3.- Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print("Ejercicio 3")        
def rgb_color_gen():
    r = random.randint(0, 255)  
    g = random.randint(0, 255)  
    b = random.randint(0, 255)  
    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form