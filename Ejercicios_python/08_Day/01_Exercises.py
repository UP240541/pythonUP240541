#1 Create an empty dictionary called dog
print("Ejercicio 1")
dog = {}

#2 Add name, color, breed, legs, age to the dog dictionary
print("Ejercicio 2")
dog['name'] = 'Zawg'
dog['color'] = 'Black'
dog['breed'] = 'Labrador'
dog['legs'] = '4'
dog['age'] = '20'
print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
print("Ejercicio 3")
studenDct = {'firstName':'Yonn', 'Lastname':'Kenedi', 'gender':'male', 'age':18, 'maritalStatus' : True, 'skills' : ['fubol','Liderazgo','Cocinar'], 'country' : 'Venezuela', 'city' : 'Caracas', 'address' : 'Calle Simon Bolivar' }
print(studenDct)

#4 Get the length of the student dictionary
print("Ejercicio 4")
print(len(studenDct))

#5 Get the value of skills and check the data type, it should be a list
print("Ejercicio 5")
print(studenDct['skills']) 
print(type(studenDct['skills']))

#6 Modify the skills values by adding one or two skills
print("Ejercicio 6")
studenDct['skills'].append("Programacion")
studenDct['skills'].append("Matematicas")
print(studenDct)

#7 Get the dictionary keys as a list
print("Ejercicio 7")
Skeys = studenDct.keys()
print(Skeys)

#8 Get the dictionary values as a list
print("Ejercicio 8")
Svalues = studenDct.values()
print(Svalues)

#9 Change the dictionary to a list of tuples using items() method
print("Ejercicio 9")
print(studenDct.items())

#10 Delete one of the items in the dictionary
print("Ejercicio 10")
print(studenDct.popitem())

#11 Delete one of the dictionaries
print("Ejercicio 11")
del dog
print(dog)

print("revisado")