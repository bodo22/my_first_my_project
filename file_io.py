print(
    f"\n\nWorking with text files\nPython has functions for creating, reading, updating, and deleting files. In the JavaScript world, you would access files using Node.js (via the fs module).\n"
)

# Open a file - will create it if not exists
# 'w' to write to file
myFile = open("myfile.txt", "w")
# Get some info
print("Name: ", myFile.name)
print("Is Closed : ", myFile.closed)
print("Opening Mode: ", myFile.mode)
# Write to file
myFile.write("I love Python")
myFile.write(" and JavaScript, ")
myFile.close()
# Append to file
myFile = open("myfile.txt", "a")
myFile.write(" I also like Golang")
myFile.close()
# Read from file
myFile = open("myfile.txt", "r+")
text = myFile.read(100)
print(text)


print(f"\n\nWorking with JSON files\n\n")

# core module
import json

#  mock JSON
userJSON = '{"first_name": "Toto", "last_name": "Doe", "age": 45}'
# Parse to dict
user = json.loads(userJSON)
# In JS:
# JSON.parse(userJSON)

print(user)
print(f"First user: {user['first_name']}")
# serialize to JSON formatted string
spaceship = {"make": "Popo", "model": "Kubwa", "year": 2070}
spaceshipJSON = json.dumps(spaceship)
# In JS:
# JSON.stringify(spaceship)

print(spaceshipJSON)
print(f"Type of carJSON{type(spaceshipJSON)}")
