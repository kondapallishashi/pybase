#This program demonstrates the difference between writing functions where the arguments are passed by reference.
#In the first method, the changes are reflected back in the calling functions
#In the second function, a local copy is made to perform calculations, there by avoiding making changes to the original value.
def calculateamount (loandetails):
    "The amount is calculated based on the load details provided with principal, rate of interest, and term as elements of the list" 
    print("The original loan details as received in calculateamount() : ", loandetails)
    print("After raising the rate of interest the loan details inside the function are:", loandetails)
    loandetails[1] = 8.5
    amount = loandetails[0]*(1+loandetails[1]*loandetails[2])
    print("The amount to be paid is :",amount)
    return

def calculateamountinflated(loandetails):
    "This function is used to calculate the amount based on inflated loan interests"
    # A local copy of the argument is made to perform required updates. 
    # This does not impact the original values outside this function.
    loandetails=[5000,10.5,3]
    print("After raising the rate of interest the loan details inside the function are:", loandetails)
    amount = loandetails[0]*(1+loandetails[1]*loandetails[2])
    print("The amount to be paid is :", amount)
    return

loandetails = [5000, 7.5, 3]
print("The original loan details in the calling function: ", loandetails)
calculateamount(loandetails)
#The interest value is updated even outside the function.
print("The loan details after calling calculateamount():",loandetails)
calculateamountinflated(loandetails)
#Since a local copy is made, the changes inside the function are not reflected here.
print("The loandetails after calling calculateamountinflated():",loandetails)

