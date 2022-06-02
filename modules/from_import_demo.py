#The from import statements allows importing the required attributes from a specific module.
#The attributes can be a functions / methods or executable code.
#This program demonstrates the importing of multiple functions from a module "functions"
from functions import generate_fibonacci, is_prime

fib_series = generate_fibonacci(10)
print("The fibonacci series generated is: ", fib_series)

#using the is_prime() function from functions module.
is_prime(25)
is_prime(19)