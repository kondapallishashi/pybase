#The functiona can optionally have arguments that are defined in the function specification.
#The function arguments can be of type, required, keyword, default and variable length arguments.
#This program demonstrates the four types of function arguments.

#The calculate amount function defines three parameters that are used to calculate loan amount
def calculateamount (principal, rate, term):
    "This function is used to calculate the amount to be paid based on simple interest calculations"
    print("Processing the required arguments")
    print("*"*50)
    amount = principal * (1 + rate * term)
    print("The loan amount to be repaid for a principal of %s, with a rate %s, for time %s is : %s"%(principal,rate,term,amount) )
    return

#This function is defined to showcase default values in function definition
def calculateamount (principal, rate=9.5, term=7):
    "This function is used to calculate the amount with default values to be paid"
    print("Processing the default arguments")
    print("*"*50)
    amount = principal * (1 + rate * term)
    print("The loan amount to be repaid for a principal of %s, with a rate %s, for time %s is : %s"%(principal,rate,term,amount) )
    return

#Function calculaterate demonstrates the usage of variable length arguments.
#The variable length argument can take 0 or more arguments.
def calculaterate(rate,*average):
    "calculaterate() calculates the average of variable length argument and prints the product of rate and average"
    print("Processing the variable length non keyword arguments")
    print("*"*50)
    sum=0
    for value in average:
        sum = sum + value
    if len(average)>0:
        average=sum/len(average)
        print("The average rate is : ", average*rate)
    else:
        print("provide more than 0 numbers to calculate the average rate")
    return

#This function is defined to demonstrate variable length keyword arguments.
#This function calculates the loan amount based on the inputs provided.
def calculate_amount_keyvar(**args):
    print("Processing the variable length keyword arguments")
    print("*"*50)
    for key,value in args.items():
        if(key == 'principal'):
            principal = value
        elif(key=='rate'):
            rate=value
        elif(key=='term'):
            term=value
    amount=principal*(1+rate*term)
    print("The amount to be paid is: ",amount)
    return


#Required Arguments
#All the arguments defined in the function are required to be included in the function call.
#If any of the argument is missed, a positional argument is missing exception is thrown.
calculateamount(3000, 7.5, 3)
#An argument is intentionally leftout. Uncomment to see exception.
#calculateamount(3000, 7.5)

#Keyword arguments
#The parameter names used in the function name can be used while calling the function. 
#using the keyword arguments allows to skip the order of arguments
calculateamount(rate=5.5,term=5,principal=5000)
calculateamount(term=2,principal=400,rate=5)

#Default Arguments
#The default values are provided for rate and term in the second function
#The function call can made by skipping the default values, if provided
calculateamount(3000)
calculateamount(3000, 2.5)
calculateamount(2000,10)

#Variable length non keyword Arguments
calculaterate(2.5)
calculaterate(3.5, 10,20)
calculaterate(3.5, 50,60,70,80,90)

#Variable length keyword arguments.
calculate_amount_keyvar(rate=5.5,term=5,principal=5000)
calculate_amount_keyvar(term=2,principal=400,rate=5)



