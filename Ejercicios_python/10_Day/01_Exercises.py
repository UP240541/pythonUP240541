#1.- Iterate 0 to 10 using for loop, do the same using while loop.
print("Ejercicio 1")
count = 0
while count < 11:
    print(count)
    count = count + 1
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers: 
    print(number)

#2.- Iterate 10 to 0 using for loop, do the same using while loop.
print("Ejercicio 2")  
count = 10
while count > -1:
    print(count)
    count = count - 1

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for number in numbers: 
    print(number)

#3.- Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print("Ejercicio 3")  
si = ["#"]
count = 0
while count < 8:
    print(si)
    si.append('#')
    count = count + 1
si.append('#')
  #
  ##
  ###
  ####
  #####
  ######
  #######

#4.- Use nested loops to create the following:
print("Ejercicio 4")  
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for fila in range(8):  
    for column in range(8):  
        print("#", end=" ")  
    print() 

#5.- Print the following pattern:
print("Ejercicio 5")  
#0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
i = 0
count = 0
while count < 11:
    mult = i*i
    print(i, "x", i, "=", mult)
    i = i + 1
    count = count + 1


#6.- Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("Ejercicio 6")  
lisa = ['Python', 'Numpy','Pandas','Django', 'Flask']
for cosas in lisa:
    print(cosas)

#7.- Use for loop to iterate from 0 to 100 and print only even numbers
print("Ejercicio 7")
for num in range(0, 101):  
    if num % 2 == 0:  
        print(num)

    

#8.- Use for loop to iterate from 0 to 100 and print only odd numbers
print("Ejercicio 8")
for num in range(0, 101):  
    if num % 2 == 0:  
        pass
    else:
        print(num)    
    

