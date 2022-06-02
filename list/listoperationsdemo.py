#Operations like + (Concatenation), * (repetition) can be performed on the elements of the Lists.
#Defining a list with just even numbers
even = [2,4,6,8,10]
#defining a list of odd numbers
odd = [1,3,5,7,9]
#concatenating the two lists
numbers = odd + even
print(numbers)
#repeat the elements of odd list two times.
numbers = odd * 2
print(numbers)
#Membership of an element can be checked using the in keyword.
print("5 is an element of the list even:", 5 in even)
print("5 is an element of the list odd:", 5 in odd)
#Elements in a list can be iterated using the for or a while loop.
for number in even:
    print(number,end="..")
