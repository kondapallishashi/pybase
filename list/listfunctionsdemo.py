#Built In Functions and Methods
even = [2,4,6,8,10]
subjects=["Math", "Physics","Chemistry","English","History"]
grades = ['A','B','C','D']
#List elements can be of any type including another list. 
student = ["John", 25, 4.5, subjects, grades, [18,16,23,24,19],"Pass"]

#Length of the list can be obtained by using the len() method.
print("The length or the number of elements in the List is len(student):", len(student))

#The min(listName) returns the minimum value of the list.
print("The min element of list even is:", min(even))
print("The min element of list subjects is:", min(subjects))
print("The min element of list grades is:", min(grades))
#The min() method can be applied on lists where elements of same type are there.
#print("The min element of list student is:", min(student))

#The max(listName) returns the maximum value of the list.
print("The max element of list even is:", max(even))
print("The max element of list subjects is:", max(subjects))
print("The max element of list grades is:", max(grades))
#The max() method can be applied on lists where elements of same type are there.
#print("The max element of list student is:", max(student))

# The list() function can be used to convert a sequence (tuple, string or any sequence) to a list
seq = (2,4,6,8)
print("A tuple can be converted to a list using the list(seq):", list(seq))
# list(2,4,6,8) --> throws an error.
print("A string can be converted to a list with each character as a list element")
print("list('python')",list('python'))
