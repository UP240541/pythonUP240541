#Exercises: Level 3
#1 Here we have a person dictionary. Feel free to modify it!
#        person={
#    'first_name': 'Asabeneh',
#    'last_name': 'Yetayeh',
#    'age': 250,
#    'country': 'Finland',
#    'is_marred': True,
#    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#    'address': {
#        'street': 'Space street',
#        'zipcode': '02210'
#    }
#    }
person={'first_name': 'Asabeneh','last_name': 'Yetayeh','age': 250, 'country': 'Finland', 'is_marred': True,
         'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'address': { 'street': 'Space street', 'zipcode': '02210'}}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skil = person['skills']
    midSkill = len(skil) // 2  
    print("El middle skill:", skil[midSkill]) 
else:
    print("Ningun skill detectado")

# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Es python en skills", True) 
    else:
        print("Es python en skills", False)
else:
    print("Ningun skill detectado")

# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
#  if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title')
#  - for more accurate results more conditions can be nested!
if 'JavaScript' and 'React' in person['skills']:
   print("He is a front end developer") 
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
        print("He is a backend depeloper")
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
        print("He is a backend depeloper")
elif 'Node' and 'React' and 'MongoDB' in person['skills']:
        print("He is a full stack developer")
else:
     print("Unknow title")   

# * If the person is married and if he lives in Finland, print the information in the following format:
#    Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] == True and 'Finland' in person['country']:
     print(person['first_name'],person['last_name'], "lives in Finland. He is married")
else:
     print("This person is not married and does not live in Finland")