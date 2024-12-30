from timeit import default_timer as timer

# myString = 'string for testing'
# myList = myString.split()

# print(myList)

# newString = ' '.join(myList)
# print(newString)

testList = ['a'] * 1000000

start = timer()
badString = ''
for i in testList:
  badString += i
end = timer()
print("Time taken: Loop = ", end - start)

start = timer()
goodString = ''.join(testList)
end = timer()
print("Time taken: Join = ", end - start)

