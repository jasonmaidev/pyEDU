from functools import reduce

# numbers = [1,2,3,4,5,6]

# result = map(lambda x: x*2, numbers)
# print(list(result))

# result = filter(lambda n : n % 2 == 0, numbers)
# print(list(result))

expenses = [
  ("groceries", 50),
  ("rent", 1200),
]

# sum = 0
# for expense in expenses:
#   sum += expense[1]

sum = reduce(lambda acc, expense: acc[1] + expense[1], expenses)


print(sum)

