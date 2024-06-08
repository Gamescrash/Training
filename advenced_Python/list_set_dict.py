
#List
numbers = [1,2,3,4,5,6,7]
even = [i for i in numbers if i%2==0]
print(even)

#Set
s = set([1,2,3,4,5,2,1,3,4,5])
print(s)
even={i for i in s if i%2==0}
print(even)

#Dict
cities = ["vibo", "roma", "modena"]
countries = ["italy", "spain", "german"]

z = zip(cities, countries)
for a in z:
    print(a)

d = {city:country for city, country in zip(cities, countries)}
print (d)