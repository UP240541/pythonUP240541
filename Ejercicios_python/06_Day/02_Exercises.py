# Exercises: Level 2

#6 Unpack siblings and parents from family_members
papa,mama, *sib = family_members
print(papa)
print(mama)  
print(sib)    


#7 Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called 
# food_stuff_tp.
fruit = ("mango", "apple", "peach")
veggie = ("tomato", "cucumber", "potato")
animalp = ("steak", "porkchop", "muttchops")
food_stufftp = fruit + veggie + animalp
print(food_stufftp)

#8 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stufflt = list(food_stufftp)
print(food_stufflt)

#9 Slice out the middle item or items from the food_stuff_tp tuple or 
# food_stuff_lt list.
midslice = food_stufftp[0:4],food_stufftp[5:] 
print(midslice)  

#10 Slice out the first three items and the last three items from
#  food_staff_lt list
firstlast = food_stufftp[2:],food_stufftp[:6] 
print(firstlast)
#11 Delete the food_stuff_tp tuple completely
del food_stufftp

#12 Check if an item exists in tuple:
print('Yonaiker' in sibTuple)

#13 Check if 'Estonia' is a nordic country
countries2 = ('China', 'Russia', 'Estonia', 'Iceland', 'Sweden', 'Norway', 'Denmark')
ch, ru, us, *scandic = countries2
print(ch)
print(ru)
print(us)
print(scandic)
print("Estonia" in scandic)

#15 Check if 'Iceland' is a nordic country
print("Iceland" in scandic)

print("revisado") #No se ejecuta