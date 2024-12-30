numbers = [1, 2, 3, 4, 5]

numbersPower2 = [n ** 2 for n in numbers]

print(numbersPower2)

# using for loop
numbersPower3 = []
for n in numbersPower2:
  numbersPower3.append(n ** 2)

print(numbersPower3)