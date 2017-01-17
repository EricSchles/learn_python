# two strings

double_quoted_string = "strings"
single_quoted_string = 'strings'

your_name = ""
your_name = "Eric"
greeting = "Hello there, "+your_name
empty_variable = None
#print(greeting)

# boolean operators

# equality ==
# less than equals <=
# greater than or equal to >=
# less than <
# greater than >
# not equal != 
print(double_quoted_string == single_quoted_string)

# print(bool(''))
# print(bool(0))
# print(bool(empty_variable))
# print(False)

# print(bool("new string"))
# print(bool(15))
# print(bool(your_name))
# print(True)

#Numbers

#Integers
print(5 + 5) # 10
print(5 - 6) # -1
print(5 * 6) # 30
print(5 / 6) # 0.8333333
print( 5 // 6) # 0

#floats
#print(5 != 5.0)
#print(5 == 5.0)
#print("5 + 5" + "=10")
#print("A"*100)
print(5 * 5.0) # 25 

# operation(Integer, float) = float
# operation(Integer, Integer) = Integer

def create_greeting(your_name):
    x = "throw away"
    return "Hello there, " + your_name

def create_greeting2(your_name, salutation="Hello there, "):
    return salutation + your_name

def simple_mean(x, y):
    return (x + y) / 2
    
print(create_greeting2("Eric", salutation="Hi! "))
print(simple_mean(5, 5))

this_list = [1,2,3]
for elem in this_list:
    print(elem)
