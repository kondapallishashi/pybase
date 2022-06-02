#This program demonstrates the basic usage of Tuples.
#Tuples are a comma seperated immutable objects, optionally enclosed between parentheses.
even = (2,4,6,8)
print("A Tuple can be created using a comma seperated objects enclosed in (), even(2,4,6,8): ",even)
odd = 1,3,5,7
print("The parentheses is optional while creating a tuple, odd = 1,3,5,7 : ",odd)
pi = 3.14, 
print("A single value tuple is created using a single object followed by comma with or without (), pi=3.14,:", pi)
subjects = ('Maths', 'Physics','Chemistry','Biology','French')
students = (odd, even, subjects)
print("A composite tuple can be created by adding tuples as elements, student=(odd, even, subjects):", students)

#The elements can be accessed using the index, which starts from 0 or using slicing with a range of indices.
print("The second element of the tuple even is even[1] : ", even[1])
print("The last element of the tuple odd is odd[-1]: ", odd[-1])
print("the first three elements of the tuple even is even[:3] : ", even[:3])
print("The last three elements of the tuple odd is odd[1:] : ", odd[1:])
print("The secord, third and fourth elements of tuple subjects is subjects[1:4]: ", subjects[1:4])

#The elements of the tuple cannot be deleted as tuples are immutable.
#The entire tuple can be deleted using the del tupleName
del even
#The below statement throws an error as tuple eve is deleted. Uncomment and try it out.
#print(even)






