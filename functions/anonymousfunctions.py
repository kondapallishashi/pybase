#This program demonstrates the usage of anonymous functions using the lamda expression.

#defining an anonymous function. Note there is no def and multi line expression function suite.
amount = lambda principal, rate, term : principal * (1 + rate * term)

#calling the anonymous functions.
print("The amount to be paid is: ",amount(2000,5.5,7))
print("The amount to be paid is: ",amount(3000,1.5,3))
