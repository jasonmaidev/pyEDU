odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

print("odds + evens = ", odds.union(evens))
print("odds & primes have in common = ", odds.intersection(primes))

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print("is all elements in setB also in setA? = ", setB.issubset(setA))

diffA = setA.difference(setB)
print("elements in setA but not in setB = ", diffA)
diffB = setB.difference(setA)
print("elements in setB but not in setA = ", diffB)

symmDiff = setA.symmetric_difference(setB) # for identifying unique values in both sets
print("elements in setA or setB but not in both = ", symmDiff) 

# setA.update(setB) # adding elements from setB to setA
# print("updated setA = ", setA)

setA.intersection_update(setB) # adding elements from in both setB and setA
print("elements in both setB and setA = ", setA)



