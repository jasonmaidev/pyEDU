class Animal:
  def walk(self):
    print("I'm walking")

class Dog(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print("Woof!")

muffin = Dog("Muffin", 3)

print(muffin.name)

muffin.walk()
muffin.bark()