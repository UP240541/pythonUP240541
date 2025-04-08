import random
#1.- Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. 
# Check the task 6 for output examples).
print("Ejercicio 1")
def list_of_hexa_colors(n):
    hex_colors = ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)]
    return hex_colors
print(list_of_hexa_colors(5))

#2.- Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print("Ejercicio 2")
def list_of_rgb_colors(n):
    rgb_colors = [f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})" for _ in range(n)]
    return rgb_colors

print(list_of_rgb_colors(5))

#3.- Write a function generate_colors which can generate any number of hexa or rgb colors.
print("Ejercicio 3")
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(n)]
    elif color_type == 'rgb':
        return [f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})" for _ in range(n)]
    else:
        return "Invalid color type. Use 'hexa' or 'rgb'."
    
print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']

print("revisado")