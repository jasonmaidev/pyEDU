try:
  result = 10/0
except ZeroDivisionError:
  print("You cannot divide by zero")
finally:
  result = 1

print(result)    