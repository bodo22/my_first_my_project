print("This is my first Python line, Yeh!")  # in JS:
# console.log('This is my first Python line, Yeh!');

# this doc is based on https://itnext.io/python-essentials-for-node-js-developers-708bb9487d70


## Variables
print("\n\Variables\n\n")


# A variable is a container for a value, which can be of various types

multiline_string = """
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes

This is also a multiline string at the same time uff
"""

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# Multiple assignment
x, y, name, is_longAndShort = (1, 2.5, "Toto", True)

# in JS:
# const x = 1, y = 2.5, name = 'Toto', is_long = true;

language = "Python"

print(language)

# multiple assignment
toto, titi, tata = (32, "grosminet", "metal")
wasgeht = True
# Variable names like in JavaScript can only start with letters or underscore (_). For variable identifiers composed of several words, you will use underscores to separate them instead of camel casing:
this_is_a_long_name = "Fernando Eduardo Juan filipo De la Hoya"

print(this_is_a_long_name)

some_dict = {
    "user": "marco",
    "adrefs": "smoe sttt.",
    "age": "hello",
    "deine": "mutter",
}


## Types And Type Casting
print("\n\Types And Type Casting\n\n")


a = 5  # int
b = 3.99  # float
c = "hi"  # str
d = True  # bool (with uppercase)
# type cqsting
a_float = float(a)
a_int = int(b)
print(a_float, a_int)


## Arithmatic Operations


# addition
print("12 + 8 =", 12 + 8)
# subtraction
print("12 - 8 =", 12 - 8)
# multiplication
print("12 * 8 =", 12 * 8)
# division
print("12 / 8 =", 12 / 8)  # js: console.log(12/8)
# exponentiation
print("12 ** 8 =", 12 ** 8)  # js: console.log(Math.pow(12, 8))
# floor division
print("12 // 8 =", 12 // 8)  # js: console.log(Math.floor(12/8))


## String Manipulation
print("\n\nString Manipulation\n\n")


a_str = "Hey, I'm a string."
b_str = "Hey, me too! "
# concat and assignment
c_str = a_str + b_str
print(c_str)
# string interpolation
print("{} eats shark for breakfast! {}".format("Toto", b_str))
print("%s eats shark for breakfast! %s" % ("Toto", b_str))
# repeat string 3 times, nice!
print(a_str * 3)
# print without new line
print(b_str, end="")
print("No line break before!")
name = "Florian"
age = 37
# Concatenate
print("Hello, my name is " + name + " and I am " + str(age))
# String Formatting
#  Positional arguments
print("My name is {name} and I am {age}".format(name=name, age=age))
# in JS:
# console.log('My name is %s and I am %i', name, age)
# F-Strings (3.6+)
print(f"Hello, my name is {{name}} {name} and I am {age}")  # <-- this is the way to go
# in JS (template literals):
# console.log(`My name is {{name}} ${name} and I am ${age}`);
# String Methods
s = "helloworld"
# Capitalize string
print(s.capitalize())
# Make all uppercase
print(s.upper())
# in JS:
# s.toUpperCase()
# Make all lower
print(s.lower())
# in JS:
# s.toLowerCase()
# Swap case
print(s.swapcase())
# Get length
print(len(s))
# in JS:
# s.length
# Replace
print(s.replace("world", "everyone"))
# in JS:
# same thing
# Count
sub = "h"
print(s.count(sub))
# Starts with
print(s.startswith("hello"))
# in JS:
# same thing
# Ends with
print(s.endswith("d"))
# in JS:
# same thing
# Split into a list
print(s.split())
# in JS:
# same thing
# Find position
print(s.find("r"))
# in JS:
# s.indexOf('r')
# Is all alphanumeric
print(s.isalnum())
# Is all alphabetic
print(s.isalpha())
# Is all numeric
print(s.isnumeric())
# in JS - careful because of coercion to number before check:
# isNaN(s)


## Lists --> JS arrays

print(
    "\n\nLists (arrays)\nA List is a collection which is ordered and changeable. Allows duplicate members. In JavaScript, they are called arrays.\n"
)


node_modules = ["express", "typescript", "nodemon", "socket.io"]
core_modules = ["fs", "path", "crypto", "https"]
# access second element in list
listEl2 = node_modules[1]
print(listEl2)
# replace element in list
core_modules[2] = "event"
print(node_modules * 2)
# print subset of list from 3rd element until end
print(core_modules[2:])
# from beginning up to but not included 4th element
print(node_modules[:3])
# multidimensional list
modules = [node_modules, core_modules]
print(modules)
# append to list
core_modules.append("net")
core_modules.append("net")
print(core_modules)
# the list grows
node_modules.insert(2, "mongodb")
print(node_modules)
# remove by value, nice!
core_modules.append("path")
core_modules.append("path")
core_modules.remove("path")
print(core_modules)
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]
# Use a constructor
numbers2 = list((1, 2, 3, 4, 5))
# In JS:
# const numbers2 = new Array(1, 2, 3, 4, 5);
# Get a value
print(fruits[1])
# Get length
print(len(fruits))
# In JS:
# fruits.length
# Append to list
fruits.append("Mangos")
# In JS:
# fruits.push('Mangos')
# Remove from list
fruits.remove("Grapes")
# In JS:
# fruits.splice(fruits.indexOf('Grapes'), 1);
# Insert into position
fruits.insert(2, "Strawberries")
# In JS:
# fruits.splice(2, 0, 'Strawberries');
# Change value
fruits[0] = "Blueberries"
# Remove with pop
fruits.pop(2)
# In JS:
# fruits.splice(2, 1);
# Reverse list
fruits.reverse()
# In JS:
# same thing
# Sort list
fruits.sort()
# In JS:
# same thing
# Reverse sort
fruits.sort(reverse=True)
# In JS:
# fruits.sort().reverse()
print(fruits)


## Tuples --> JS "frozen Array"
print(
    "\n\nTuples\nSimilar to lists to the exception that they cannot be modified after they are created (immutable). A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.\n"
)


# Create tuple
fruits = ("Apples", "Oranges", "Grapes")
# In JS, does not exist but you can create objects with unchangeable properties
# let fruits = Object.defineProperties({}, {
#     0: {
#         value: "Apples",
#         writable: false
#     }, 1: {
#         value: "Oranges",
#         writable: false
#     }, 2: {
#         value: "Grapes",
#         writable: false
#     }
# });
# Using a constructor
fruits2 = tuple(("Apples", "Oranges", "Grapes"))
# Single value needs trailing comma
fruits2 = ("Apples",)
# In JS, does not exist but you can create objects with unchangeable properties
# const fruits = Object.defineProperty({}, 0, {
#   value: "Apples",
#   writable: false
# });
# Get value
print(fruits[1])
# Can't change value
try:
    fruits[0] = "Pears"
except:
    print("successfully didnt work")
# Delete tuple
del fruits2
# In JS, delete a reference:
# delete fruits2
# Get length
print(len(fruits))


## Sets --> JS Sets

print(
    "\n\nSets\nA Set is a collection which is unordered and unindexed. No duplicate members. The Set data structure is also available in JavaScript since ES6.\n"
)

# Create set
fruits_set = {"Apples", "Oranges", "Mango"}
# In JS:
# const fruitsSet = new Set(['Apples', 'Oranges', 'Mango'])
# Check if in set
print("Apples" in fruits_set)
# In JS:
# fruitsSet.has('Apples')
# Add to set
fruits_set.add("Grape")
fruits_set.add("Grape")
fruits_set.add("Grape")
print(fruits_set)
# In JS:
# same thing
# Remove from set
fruits_set.remove("Grape")
print(fruits_set)
# In JS:
# fruitsSet.delete('Grape')
# Add duplicate, will not add
fruits_set.add("Apples")
print(fruits_set)
# Clear set = empty set
fruits_set.clear()
print(fruits_set)
# In JS:
# same thing
# Delete / dereference
del fruits_set
# In JS, cannot use the delete operator on a set:
# fruitsSet = undefined
# throws not defined error
try:
    print(fruits_set)
except:
    print("successfully didnt work")


## Dictionaries --> JS Objects
print(
    "\n\nDictionaries\nA Dictionary is a collection of key/value pairs which is unordered, changeable and indexed. No duplicate members. Similar to plain old JavaScript objects. You must use quotes for the keys; in JavaScript, it is optional.\n"
)

# Create dict
person = {"first_name": "Eoto", "last_name": "Doe", "age": 30}
# Use constructor
person2 = dict(first_name="Malua", last_name="Eolofu")
# In JS:
# let person2 = Object.defineProperties({}, {
#     first_name: {value: 'Malua'},
#     last_name: {value: 'Eolofu'},
#     age: {value: 453}
# });
# let person2 = Object.create(); / new Object();
# person2.first_name = 'Malua';
# person2.last_name = 'Eolofu';
# person2.age = 453;
# Get value
print(person["first_name"])
print(person.get("last_name"))
print(person.get("middle_name", "default middle name"))
# In JS:
# the same or person.first_name

# Add key/value
person["phone"] = "555-555-5555"
# In JS:
# the same  or person.phone = 555-555-5555'

# Get dict keys
# returns a dict_keys object, not a list
# to get list: list(person.keys())
print(person.keys())
# In JS:
# Object.keys(person)

# Get dict items
# returns a dict_items object, not a list
# to get list: list(person.items())
print(person.items())
# In JS:
# Object.values(person)

# Copy dict
person2 = person.copy()
person2["city"] = "Boston"
# In JS:
# person2 = {...person};

# Remove item
del person["age"]
person.pop("phone")
# In JS:
# delete person.age;

# Clear
person.clear()
print(f"person: {person}")
# In JS, does not exist:
# person = {};
# you can empty all values but keep the keys:
# for(let p in person) Object.defineProperty(person, p, {value: undefined});

# Get length
print(len(person2))
# In JS:
# Object.keys(person2).length
# Object.values(person2).length
# Object.entries(person2).length

# List of dict
people = [{"name": "Tutu", "age": 30}, {"name": "Soso", "age": 25}]
# In JS:
# same things
print(people[1]["name"])


## Functions -> JS Functions
print(
    "\n\nFunctions\nA function is a block of code which only runs when called. In Python, we do not use curly brackets, we use indentation with tabs or spaces. If you don’t respect the indentation rules, your program will crash ! Would be nice to have in JS to force devs to write clean code !\n"
)

# Create function with default parameter value
def sayHello(name="Floriam"):
    print(f"Hello {name}")


# In JS:
# function sayHello(name='Floriam') {
#     console.log(`Hello ${name}`);
# }


# call function
sayHello()
# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total


# In JS
# function getSum(num1, num2) {
#   const total = num1 + num2;
#   return  total;
# }
sum = getSum(11, 99)
print(sum)


## Lambda Functions --> JS Arrow functions

print(
    "\n\nLambda Functions\nA lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression. Very similar to JavaScript arrow functions.\n"
)

getSum = lambda num1, num2: num1 + num2

# doesnt work:
# getSum = lambda (num1, num2):
#    return num1 + num2
# getSum = lambda num1, num2:
#    return num1 + num2
# getSum = lambda num1, num2:
#    num1 + num2
# getSum = lambda num1, num2: return num1 + num2

# In JS
# let getSum = (num1, num2) => num1 + num2
print(getSum(10, 3))


## Conditionals --> JS conditionals
print(
    "\n\nConditionals\nIf/ Else statements are used to decide to do something based on a condition being true or false. In Python, no parentheses around the condition.\n"
)

x = 43
y = 22
# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# Simple if
if x > y:
    print(f"{x} is greater than {y}")
# if(x > y)...
# If/else
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is not greater than {x}")
# elif
if x > y:
    print(f"{x} is greater than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{y} is less than {x}")
# Nested if's
if x > 2:
    if x <= 10:
        print(f"{x} is greater than 2 and less than or equal to 10")


## Logical Operators -> JS logical operators
print(
    "\n\nLogical Operators (==, !=, >, <, >=, <=)\nLogical operators (and, or, not) — Used to combine conditional statements. Python lexical style is more human friendly.\n"
)

x = 43
y = 22
# and
if x > 2 and x <= 10:
    print(f"{x} is greater than 2 and less than or equal to 10")
# In JS:
# if( x > 2  &&  x <= 10 )...
# or
if x > 2 or x <= 10:
    print(f"{x} is greater than 2 or less than or equal to 10")
# In JS:
# if ( x > 2 || x <= 10 )...
# not
if not (x == y):
    print(f"{x} is not equal to {y}")
# In JS:
# if ( x !== y )...


## Membership Operators
print(
    "\n\nMembership Operators\nMembership operators are used to test if a value exists in a sequence or not.\n"
)

x, y, numbers = (43, 22, [1, 2, 3, 4, 5, 43])
#  in
if x in numbers:
    print(f"{x} is in numbers: {x in numbers}")
# not in
if x not in numbers:
    print(f"{x} is not in numbers: {x not in numbers}")
print(f"outside if not in: {x} is not in numbers: {x not in numbers}")


## Loops
print("\n\nLoop\n\n")

people = ["John", "Paul", "Sara", "Susan"]
# Simple for loop
for person in people:
    print(f"Current Person: {person}")
# Un JS, for...of to iterate over iterables (array, set...)
# for(person of people)...


# Break
for person in people:
    if person == "Sara":
        print(f"Current Person break: {person}")
        break
# In JS
# same thing


# Continue
for person in people:
    if person == "Sara":
        print(f"Current Person continue: {person}")
        continue
# In JS
# same thing


# range
for i in range(len(people)):
    print(f"Current Person in range: {people[i]}")
# In JS, does not exist:
# for(let i = 0; i < people.length; i++)...
# OR people.forEach((person, index) => {...})
# OR for( n of [...people.keys()] )...
# OR set a global custom method
# Array.range = (start, end) => Array.from({length: (end - start)}, (v, k) => k + start);
for i in range(0, 11):
    print(f"Number: {i}")
# In JS,:
# for( n of [...Array(11).keys()])...


# While loops execute a set of statements as long as a condition is true.
count = 0
while count < 10:
    print(f"Count: {count}")
    count += 1
# In JS
# same thing


## Modules
print(
    "\n\nModules\nLike in Node.js, a module is basically a file containing a set of functions to include in your application. There are core Python modules, modules you can install using the pip package manager (including Django) as well as custom modules.\n"
)

import module_example

## Classes
print(
    f"\n\nClasses\nA class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object. In case you didn’t know (shame if you work daily with JavaScript…), JS is a prototype-oriented language. Everything is an object in JavaScript but properties on objects (other than its own) are accessed via the prototype chain lookup mechanism (prototypal inheritance — not class inheritance). Moreover objects in JS are created via constructor functions (the ES6 classes are syntax sugar — not class constructs like in other languages). You will notice that in Python, you don’t need the new operator to instantiate objects from a class.\n"
)


email = "test@example.com"

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"

    def has_birthday(self):
        self.age += 1


# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    # method overring
    def greeting(self):
        return f"My name is {self.name} and I am {self.age} and my balance is {self.balance}"


#  Init user object
florian = User("Florian GOTO", "florian@gmail.com", 99)
# Init customer object
tatu = Customer("Tatu KENYATTA", "tatu@yahoo.com", 25)
tatu.set_balance(500)
print(tatu.greeting())
florian.has_birthday()
print(florian.greeting())
