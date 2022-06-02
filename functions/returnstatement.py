#This program demonstrates the usage of return statement with an expression.
def calculateamount(principal, rate, term):
    "This function calculates the amount to be paid based on simple interest calculations"
    amount = principal * (1 + rate * term)
    return amount
    #both the above expressions can be combined.
    #comment the two expressions and uncomment the below expression to try it out.
    #return principal * (1 + rate * term )
    
# To call a function that returns a value or an expression, define a variable to receive the value.
amount = calculateamount(3000, 5.5, 7)
print("The amount to be paid is: ", amount)
