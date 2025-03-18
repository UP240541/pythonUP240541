#1 Create an empty tuple
mtTuple = ()

#2 Create a tuple containing names of your sisters and your 
# brothers (imaginary siblings are fine)
sibTuple = ("Yuleinis", "Yonaiker", "Davielis", "Leidi")
print(sibTuple)
#3 Join brothers and sisters tuples and assign it to siblings
broTuple = ("Nicotricio", "Wuainer", "Jhon Daniel", "Jairo", "Alfredo")
sisTuple = ("Yalitzia", "Yoselin", "Yeraldin", "Yuneidis", "Dianela")
sibTuple = broTuple + sisTuple
print(sibTuple)

#4 How many siblings do you have?
print(len(sibTuple))

#5 Modify the siblings tuple and add the name of your father and mother
#  and assign it to family_members
family_members = ("Ovimarlixion", "Yusleidi")
family_members = family_members + sibTuple
print(family_members)

