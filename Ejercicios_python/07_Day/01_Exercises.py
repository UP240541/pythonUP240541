# Exercises: Level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Find the length of the set it_companies
print("Ejercicio 1")
print(len(it_companies))

#2 Add 'Twitter' to it_companies
print("Ejercicio 2")
it_companies.add('Twatter')

#4 Insert multiple IT companies at once to the set it_companies
print("Ejercicio 3")
it_companies.update(['Tencent','Meta','Intel'])
print(it_companies)

#5 Remove one of the companies from the set it_companies
print("Ejercicio 4")
it_companies.remove('Facebook')
print(it_companies)

#6 What is the difference between remove and discard
print("Ejercicio 5")
print("Podemos remover items no especificados con discard(), en cambio remove() da error")
it_companies.pop()
print(it_companies)

print("revisado")
