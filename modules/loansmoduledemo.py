#This program demonstrates the concept of modules.
#In this program, loans module is imported and code/functions defined in this module is reused.
#Import loans module
import loans

amount = loans.calculate_amount(5000,3.5,6)
print("The loan amount is: ", amount)