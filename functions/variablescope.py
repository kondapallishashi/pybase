#This function demonstrates the scope of variables. 
#Python supports global and local scopes.
#Variables declared within a function or a suite are local variables and can only be accessed within that suite.
#variables declared outside are global variables and can be accessed across the program.

#All the below variables are global variables and can be accessed across the program.
principal = 25000
rate = 7.2
term = 3
amount = 0

if principal > 15000 :
    #amount, principal, rate, term are global variables and can be accessed here.
    amount = principal * (1 + rate * term)
    #any variable defined with in a suite is local variable.
    inflatedrate = 8.5
    adjustedterm = 5
    forecastedamount = principal * (1 + inflatedrate * adjustedterm)
    print("The original amount to be paid is : ", amount)
    print("The forecasted amount to be paid is : ", forecastedamount)

#Attempting to access the local variables here will thrown an exception. 
#Uncomment and tryout
#print("The local variables are not accessible here:", inflatedrate)
#print("The local variables are not accessible here:", adjustedterm)
#print("The local variables are not accessible here:", forecastedamount)

def yearlypayments():
    #amount, principal, rate, term being global variables can be accessed here.
    amount = principal * (1 + rate * term)
    #Interest, yearlyinterest are local variables and can be accessed only with in yearlypayments()
    interest = amount - principal
    yearlyinterest=interest/term
    print("The overall interest is: ", interest)
    print("The yearly interest is: ", yearlyinterest)
    
#call the yearlypayments()
yearlypayments()
    
#Any attempt to access local variables interest, yearlyinterest will throw an exception.
#Uncomment and tryout
#print("The local variables are not accessible here:", interest)
#print("The local variables are not accessible here:", yearlyinterest)