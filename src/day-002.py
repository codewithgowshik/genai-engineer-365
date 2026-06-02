# Variables
# Variables are used to store datas
user_name = 'Gowshik' 
user_age = 18

#Data Types
# Avoid using Python built-in names as variables
text_value = "used to write a string"
integer_value = 2
boolean_value = True
float_value = 2.1

# print is an output statement and input is an input statement both are keywords in python.

# f-strings.
#Inserts variables directly into strings.
age = 18 
print(f'my name is gowshik, I am {age} old.')

# functions - Reusable blocks of code
def myname():
  print('gowshik')
myname() #calling a function here 

# with parameters
def greet(name):
    print(f"hello {name}")
greet("gowshik")

#with return function
#return - sends value back from the function 
def add(a,b):
  return a + b 
final_output  = add(10 , 10)
print(final_output)

#type hint 
#syntax : def function(parameter: type) -> return_type:
def add(a: int, b: int) -> int:
    return a + b
#Type hints describe what type of data a function expects and what type it returns. 
#They make code easier to read and understand.
