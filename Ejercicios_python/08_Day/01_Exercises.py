#1 Create an empty dictionary called dog
dog = {}

#2 Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Zawg'
dog['color'] = 'Black'
dog['breed'] = 'Labrador'
dog['legs'] = '4'
dog['age'] = '20'
print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
studenDct = {'firstName':'Yonn', 'Lastname':'Kenedi', 'gender':'male', 'age':18, 'maritalStatus' : True, 'skills' : ['fubol','Liderazgo','Cocinar'], 'country' : 'Venezuela', 'city' : 'Caracas', 'address' : 'Calle Simon Bolivar' }
print(studenDct)

#4 Get the length of the student dictionary
print(len(studenDct))

#5 Get the value of skills and check the data type, it should be a list
print(studenDct['skills']) 
print(type(studenDct['skills']))

#6 Modify the skills values by adding one or two skills
studenDct['skills'].append("Programacion")
studenDct['skills'].append("Matematicas")
print(studenDct)

#7 Get the dictionary keys as a list
Skeys = studenDct.keys()
print(Skeys)

#8 Get the dictionary values as a list
Svalues = studenDct.values()
print(Svalues)

#9 Change the dictionary to a list of tuples using items() method
print(studenDct.items())

#10 Delete one of the items in the dictionary
print(studenDct.popitem())

#11 Delete one of the dictionaries
del dog

