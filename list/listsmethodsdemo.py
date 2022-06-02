#This program demonstrates the ket methods supported by List.
#Define two Lists
subjects=["Maths","Physics","Chemistry","Computers","Biology","French"]
distances = [34,87,400,34,206,876,15,97,34,358,15,206]
stringSequence = ("History","English", "Civics")
numberSequence = (2,4,6,8)

#Appending an element to the end of the list using list.append(obj)
#providing more than one argument in the append() method throws an error.
print("Appending 'English' to the end of subjects list, subjects.append('English'):",subjects.append('English'),"\n",subjects)
print("Append 999 to the list using distances.append(999) and print updated list", distances.append(999),"\n",distances)

#The number of occurances of an element can be counted using the list.count(obj)
print("The number times 34 occurs in the list is distances.count(34):",distances.count(34))
print("The number times 15 occurs in the list is distances.count(15):",distances.count(15))
print("The number times 'Math' occurs in the list is subjects.count('Maths'):",subjects.count('Maths'))

#The list can be extended by adding the elements of a sequence using the list.extend(seq) method.
print("extending the subjects list by adding stringSequence, subjects.extend(stringSequence): Returns:",subjects.extend(stringSequence),"\n", subjects)
print("Extending distances,distances.extend(numberSequence): Returns: ", distances.extend(numberSequence),"\n",distances)
print("The extend method can be provided with a list as an argument, distances.extend(list(numberSequence)): ",distances.extend(list(numberSequence)),"\n",distances)

# The lowest index of the occurance of the element is obtained using list.index(obj)
print("The element 15 in distances list is at : ",distances.index(15))
#1000 is not in the list, so the below statement throws an exception
#print("The element 1000 in distances list is at : ",distances.index(1000))
print("The element 'Chemistry' in the subjects list is at:", subjects.index('Chemistry'))

#An element can be inserted into the list at a valid index using list.insert(index,obj)
print("Inserting 1000 at index 3, ie fourth position, distances.insert(3,1000): Returns:",distances.insert(3,1000),"\n",distances)
print("Providing a Wrong index inserts element at the end of the list, distances.insert(50,99): Returns:",distances.insert(50,99),"\n",distances)
print("Inserting 'C#' at index 5, ie sixth position, subjects.insert(5,'C#'): Returns:",subjects.insert(5,'C#'),"\n",subjects)

#An element is removed and returned from the list using the list.pop(obj=list[-1])
print("Removing the last element from the list using distances.pop(): ", distances.pop(),"\n",distances)
print("Removing the third element from the list using distances.pop(2): ", distances.pop(2),"\n",distances)
print("Removing the last element from the list using subjects.pop(): ", subjects.pop(),"\n",subjects)

#An element can be removed from the list using the list.remove(obj) method.
print("Removing element 999 from the distances list, distances.remove(999): Returns: ", distances.remove(999), "\n",distances)
print("Removing element 'C#' from the subjects list, subjects.remove('C#'): Returns: ", subjects.remove('C#'), "\n",subjects)

#The elements order can be reversed using the list.reverse() method.
print("The order of elements in list can be reversed using distances.reverse(), Returns: ", distances.reverse(), "\n", distances)
print("The order of elements in list can be reversed using subjects.reverse(), Returns: ", subjects.reverse(), "\n", subjects)

#The elements in the list can be sorted using the list.sort() method.
print("The elements in the list can be sorted using the distances.sort(), Returns: ", distances.sort(), "\n", distances)
print("The elements in the list can be sorted using the distances.sort(), Returns: ", subjects.sort(), "\n", subjects)