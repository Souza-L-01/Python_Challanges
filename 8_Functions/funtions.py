# Functions
# What are Functions?
# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.

def my_function():
    print("Hello From My Function!")    

def my_function_with_args(username, greeting):
    print("Hello, %s, From my function! I wish you %s" % (username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function("HI")
    print("%s" % simple_greeting)

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")
    print("Hello %s, I wish you %s" % (username, greeting))

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
    print(x)
    
# Modify this function to return a list of strings as defined above
def list_benefits():
    return []

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return ""

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()