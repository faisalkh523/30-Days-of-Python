# Exercise: Level 2

# Question 1: Check the python version you are using

# Answer : from the vscode terminal running the command: python --vesrion, gives: 3.12.7

# Question 2
a = 3
b = 4

addition = a+b
subtraction = a-b
multiplication = a*b
modulus = a%b
division = a/b
exponential = a**b
floor_division = a//b

# outputs
print(addition)
print(subtraction)
print(multiplication)
print(modulus)
print(division)
print(exponential)
print(floor_division)


# Question 3: Write strings on the python interactive shell. The strings are the following:
my_name = "Faisal"
my_family_name = "Hassan"
my_country = "Nigeria"
comment = "i am enjoying 30 days of python"

# outputs
print(my_name)
print(my_family_name)
print(my_country)
print(comment)

# Question 4: Check the data types of the following data
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'python', 'Finland']))
print(type('Your name'))
print(type('Your family name'))
print(type('Your country'))

# Exercise: Level 3

# Question 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# Number(integer, Float, complex), String, Boolean,List, Tuple, Set and Dictionary.

# Answer
# Numbers
integers = {1, 3, 4}
float = {2.4, 3.5, 5.6}
complex = (2-2j)

#String
string = "Faisal"
# Boolean
boolean = True 
#List
list = ['house', 2, 'orange']
# Tuple
tuple = ('orange', 'mango', 'apple')
# Set
Set = {1, 3, 5}
# Dictionary
dictionary = {'computer': 4000, "phone": 2500}

# Output
print(integers)
print(float)
print(complex)
print(string)
print(boolean)
print(list)
print(tuple)
print(set)
print(dictionary)




# Question 2. Find an Euclidian distance between (2,3) and (10,8)
import numpy as np

# writting the distance point in a list
first_point =  [2, 3]
second_point =  [10, 8]

# cslculating distance
distance = np.sqrt (((second_point[0] - first_point[0])**2) + ((second_point[1] - first_point[1])**2))

# Printing the result
print('Euclidian distance=', distance)