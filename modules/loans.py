#This program demonstrates a simple module. 
#Define three or more methods that logically relate to each other.
#Considering a loan scenario, three methods are defined in this module.

def calculate_amount(principal, rate, term):
    "This function takes in principal, rate and term as arguments and calculates the loan amount"
    amount = principal * (1 + rate * term)
    return amount
    
def calculate_interest(amount, principal):
    "This function takes amount and principal as arguments and calculates interest"
    return amount - principal

def generate_risk_details(credit_score):
    if credit_score > 10:
        print("The credit history of the customer is good and loan is at no risk")
    elif credit_score < 8 & credit_score > 5:
        print("The credit history of the customer is moderate and loan is at moderate risk")
    else:
        print("The credit history of the customer is not good and loan is at high risk")
        