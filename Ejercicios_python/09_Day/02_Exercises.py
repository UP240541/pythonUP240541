#Exercises: Level 2
#1 Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F
calf = int(input("Ingrese su calificacion: "))
if calf >= 90 and calf <= 100:
    print("Tu calificacion de", calf, "equivale a una A")
elif calf >= 70 and calf <= 89:   
    print("Tu calificacion de", calf, "equivale a una B")
elif calf >= 60 and calf <= 69:   
    print("Tu calificacion de", calf, "equivale a una C")
elif calf >= 50 and calf <= 59:   
    print("Tu calificacion de", calf, "equivale a una D")
elif calf >= 0 and calf <= 49:   
    print("Tu calificacion de", calf, "equivale a una F")   
else:
    print("Error")     

#2 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer
season = str(input("Ingrese un mes: "))
if season in ["Septiembre","Octubre", "Noviembre"]:
    print(season, "esta en otoño")
elif season in ["Diciembre", "Enero", "Febrero"]:
    print(season, "esta en invierno")
elif season in ["Marzo", "Abril", "Mayo"]:
    print(season, "esta en primavera")
elif season in ["Junio", "Julio", "Agosto"]:
    print(season, "esta en verano")
else:
    print("Error")     


#3 The following list contains some fruits:
#```sh
#fruits = ['banana', 'orange', 'mango', 'lemon']
#```
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
#  If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = str(input("Ingrese una fruta: "))
if fruta in fruits:
    print("Esa fruta ya exite")
else:
    fruits.append(fruta)
    print(fruits)

print("revisado")