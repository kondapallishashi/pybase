#Since the tuples are immutable, any change to the original tuple is not possible.
#However, a new tuple with the required changes can be created.
even = (2,4,6,8)
odd = 1,3,5,7
subjects = ('Maths', 'Physics','Chemistry','Biology','French')
#The below statement throw errors. Uncomment and tryout.
#even[1]=10

numbers = odd + even
print("A new tuple is created by concatenating odd and even tuples is, numbers = odd + even: ",numbers)
repeatEven = even * 2
print("The elements of the tuple even can be repeated twice using even *2: ", repeatEven)
margin = numbers[2:6]
print("A new tuple with required range of elements can be created as margin = numbers[2:6] : ", margin)

#The existence of an element can be determined using the in operator.
print("Is 5 an element of tuple even, 5 in even: ", 5 in even)
print("Is 5 an element of tuple odd, 5 in odd: ", 5 in odd)
print("Is 'Chemistry' part of subjects tuple, 'Chemistry' in subjects : ", 'Chemistry' in subjects)

#The elements in a tuple can be iterated using a for loop or a while loop
for subject in subjects:
    print(subject, end =' ' )
    

