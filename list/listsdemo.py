#Defining Lists
even = [2,4,6,8,10]
subjects=["Math", "Physics","Chemistry","English","History"]
grades = ['A','B','C','D']
#List elements can be of any type including another list. 
student = ["John", 25, 4.5, subjects, grades, [18,16,23,24,19],"Pass"]
print(student)
#Lists can be generated using list(seq) where seq could be a sequence, tuple or a string.
employee = ("Dave","MS",32,"Programmer", 60000)
print("The tuple created to be converted to List is:", employee)
employeeList = list(employee)
print("The elements of tuple employee converted to employeeList, employeeList:", list(employee))
text = "sample string"
print("List can be constructuted using list(string) method: ", list(text))
#Lists can be generated using the range() generator method as well.
print("The list of numbers ranging from 0 to 4 is list(range(5)):", list(range(5)))

#Accessing elements in the list
#Accessing the elements using the index values.
print("The first element of List student can be accessed using student[0]:",student[0])
print("The fourth element of List student can be accessed using student[0]:",student[3])
print("Negative indices can be used to access elements from the end:\nstudent[-1]:",student[-1])

#Access a range of elements using slicing with List[start:end]. End is not inclusive.
print("The first 3 elements of the list: student[0:3]:",student[0:3])
print("The first 3 elements of the list: student[:3]:",student[:3])
print("All the elements from 3 element to the end of list: student[2:]:",student[2:])
#Updating the elements of the List:
student[1] = 26
print("The updated student list is:", student)
student[3] = ["Math","physics","chemistry","Computers","English"]
print("The updated student list is:", student)
#del student[1]
print("The updated student list is:", student)
#del student[1:4]
print("The updated student list is:", student)
