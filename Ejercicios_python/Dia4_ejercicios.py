#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
no = 'Thirty'
time = 'Days'
space = ' '
conect = "Of"
lengua = "Python"
conca = no  +  space + time + space + conect + space + lengua
print(conca)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
verb = 'Coding'
adj = 'All'
conect2 = "For"
conca2 = verb + space + conect2 + space + adj
print(conca2)

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = conca2

#4 Print the variable company using print().
print (company)

#5 rint the length of the company string using len() method and print().
print(len(company))

#6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string.
cortada = company[6:] 
print(cortada)

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_string = 'Coding'
print(company.index(sub_string))  
print(company.find('Coding'))  

#11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python')) 

#12 Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace('Coding For All', 'Python For Everyone')) 

#13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split()) 
company = 'Coding For All'
print(company.split(' ')) 

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
ej14 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(ej14.split())
ej14 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(ej14.split(','))

#15 What is the character at index 0 in the string Coding For All.
print(company[0]) 

#16 What is the last index of the string Coding For All.
print(company[13])
#17 What character is at index 10 in "Coding For All" string.
print(company[10])
#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym1 = "PFE"

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
acronym2 = "CFA"

#20 Use index to determine the position of the first occurrence of C in Coding For All.
sub_string = 'C'
print(company.index(sub_string)) 

#21 Use index to determine the position of the first occurrence of F in Coding For All.
sub_string1 = 'F'
print(company.index(sub_string1)) 

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
occurrence = 'You cannot end a sentence with because because because is a conjunction'
print(occurrence.find('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sub_string2 = 'because'
print(occurrence.rindex(sub_string2))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_because = occurrence[0:31]
print(first_because)
last_because = occurrence[54:]
print(last_because) 

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(occurrence.find('because'))


#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_because = occurrence[0:31]
print(first_because)
last_because = occurrence[54:]
print(last_because) 

#28 Does 'Coding For All' start with a substring Coding?
print("Coding for all empieza con el substring Coding")
print(company.startswith('Coding')) 

#29 Does 'Coding For All' end with a substring coding?
print("Coding for all termina con el substring Coding")
print(company.endswith('Coding')) 

#30 '      Coding For All      '  , remove the left and right trailing spaces in the given string.
company30 = '      Coding For All      '
print(company30.strip('       '))

#31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print(var1.isidentifier())
print(var2.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.
lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " # ".join(lib)
print(result)

#33 Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print('I\nam\nenjoying\nthisnchallenge')
print('I\njust\nwonder\nwhat\nis\nnext.')

#34 Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

#35 se the string formatting method to display the following:
# The area of a circle with radius 10 is 314 meters square.
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

#36 Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144

a = 8
b = 6
suma = a + b
resta = a - b
multi = a * b
divi = a / b 
porce = a % b
divf = a // b
elev = a ** b

formated_string2 = '{} + {} es {}'.format(a,b,suma)
formated_string3 = '{} - {} es {}'.format(a,b,resta)
formated_string4 = '{} * {} es {}'.format(a,b,multi)
formated_string5 = '{} / {} es {:.2f}'.format(a,b,divi)
formated_string6 = '{} % {} es {}'.format(a,b,porce)
formated_string7 = '{} // {} es {}'.format(a,b,divf)
formated_string8 = '{} ** {} es {}'.format(a,b,elev)
print(formated_string2)
print(formated_string3)
print(formated_string4)
print(formated_string5)
print(formated_string6)
print(formated_string7)
print(formated_string8)