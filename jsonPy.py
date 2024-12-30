import json

# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# personJSON = json.dumps(person, indent=4)

# print(personJSON)

# writting json data to file
# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)

# decoding json data
# with open("person.json", "r") as jsonFile: #read from file
#   person = json.load(jsonFile)
#   print(person)

class User:
    # Custom class with all class variables given in the __init__()
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Jack", 30)