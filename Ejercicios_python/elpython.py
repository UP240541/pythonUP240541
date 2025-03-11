#The following is a list of 10 students ages:
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
#Add the min age and the max age again to the list
#Find the median age (one middle item or two middle items divided by two)
##Find the average age (sum of all items divided by their number )
#Find the range of the ages (max minus min)
#Compare the value of (min - average) and (max - average), use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
minage = ages[0] 
print(minage)      
last_index = len(ages) - 1
maxage = ages[last_index]
print(maxage)

#import paises as pis
#paises = pis.countries
#print(pis.countries)

