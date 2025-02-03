#Integer (int)
# Represents whole numbers, both positive and negative.
# Example: 1, 2, 3, -1, -2, -3
X = 10 
print(X)  # Output: 10

# integer numbers you can modify to string 
my_int = 100 
my_str = str (my_int)
print (type(my_str))
# if you need to know the type of the variable you can write type 

# ***************************
# Float (float)
# Represents decimal numbers.
# Example: 1.0, 2.0, 3.0, -1
print(10.5)  # Output: 10.5

# ******************************
# String (str)
# Represents a sequence of characters.
# Example: "Hello", 'Hello', "Hello World", 'Hello World'

Mystring = " hellow world "
print(Mystring)  # Output: hellow world

#**********************************************
# Boolean (bool)
# Represents a logical value, either True or False.
its_student = True
print(its_student) # Output: True

# ******************************************
# List (list)
# Represents a collection of items which can be of any data type, including strings, integers, floats
# Example: [1, 2, 3], ["apple", "banana", "ch"], [1, 2, "three"]

my_list = [1,3 , "cali", "ahmed"]
print(my_list) # Output: [1, 3, 'cali', 'ahmed']

# **********************************************
# Tuple (tuple)
# Represents a collection of items which can be of any data type, including strings, integers, floats
# Example: (1, 2, 3), ("apple", "banana", "ch")
my_tuple = (1, 3, "cali", "ahmed")
print(my_tuple) # Output: (1, 3, 'cali', 'ahmed)


# ***********************************************
# Dictionary (dict)
# Represents a collection of key-value pairs. Each key is unique and maps to a specific value.
# Example: {"name": "John", "age": 30}, {"city": "New"}
my_dict = {"name": "ahmed", "age": 30, "city": "cali"}
print(my_dict) # Output: {'name': 'ahmed', 'age': 30, 'city': '}

# converting to a dictionary
my_dict = dict(name="ahmed", age=30, city="cali")
print(my_dict) # Output: {'name': 'ahmed', 'age': 30, 'city': 'cali'}
# if you need to know the type of the variable you can write type()  # Output: <class 'dict'>
print(type(my_dict)) # Output: <class 'dict'>

# ***************************************************
# Set (set)
# Represents a collection of unique items.
# Example: {1, 2, 3}, {"apple", "banana", "ch"}
my_set = {1, 3, "cali", "geedi"}
print(my_set) # Output: {1, 3, 'cali', 'geedi'}


# casting - Represents a conversion of a variable from one data type to another.
# Example: int("123"), float("123.45"), str(123), bool(1)
# casting to integer
print(int("123")) # Output: 123

my_int = "123"
print(int(my_int)) # Output: 123

# casting to float
print(float("123.45")) # Output: 123.45

my_float = "123.45"
print(float(my_float)) # Output: 123.45

# casting to string
print(str(123)) # Output: '123'

my_string = 1234
my_str = str(my_string)
print(str(my_str)) # Output: '1234'
print(type(my_str)) # Output: <class 'str'>

# casting to boolean
print(bool(1)) # Output: True
# casting to boolean
print(bool(0)) # Output: False
# ***********************************************

# casting to list 
# converting a string or tuple to a list

str_data = "hellow"
list_data = list(str_data)
print(list_data) # Output: ['h', 'e', 'l', 'l', 'o']

tuple_list = (1, 2, 3, 5, 6)
list_data_tuple = list(tuple_list)
print(list_data_tuple) # Output: [1, 2, 3, 5, 6]

# To convert a list or string to a tuple:

list_data = [1, 2, 3, 4, 5]
my_tuple = tuple(list_data) 
print(my_tuple) # Output: (1, 2, 3, 4, 5)

str_data = "hellow world"
tuple_data = tuple(str_data)
print(tuple_data) # Output: ('h', 'e', 'l', 'l', 'o', ' ','w', 'o', 'r', 'l', 'd')
# ***********************************************

