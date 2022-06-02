#This program defines a new module with some key functions defined in it. 
#This is like a library file where multiple functions can be defined and reused.

#Functions Module where multiple utility functions are to be written
#Define the function that generates the fibonacci series up to given number n.
def generate_fibonacci(limit): 
    "Takes an upper limit as parameter and returns Fibonacci series up to n in a list"
    #define an empty list
    fibonacci_series = []
    x, y = 0, 1
    while y < limit:
        fibonacci_series.append(y)
        x=y
        y=x+y
        #Optimized statement below: comment above two lines and uncomment the below statement.
        #x,y = y,x+y
        
    return fibonacci_series
    
#Define a function that evaluates a given number and returns whether its a prime number or not.    
def is_prime(number):
    # define a flag variable
    flag = False
    # prime numbers are greater than 1
    if number > 1:
    # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    
        # check if flag is True
        if flag:
            print(number, "is not a prime number")
        else:
            print(number, "is a prime number")
