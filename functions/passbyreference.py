def updatemarks(markslist) :
    "This function updates the elements of the lists passed as argument"
    print("The original marks scored as received in the updatemarks()", markslist)
    markslist[2] = 20
    markslist[5] = 20
    print("The updated marks list as seen inside the update function :",markslist)
    return

#Define a markslist list with marks scored in 6 subjects.
markslist = [18,16,19,23,15,17]

print("The original marks scored :", markslist)
#Call the updatesmarks function
updatemarks(markslist)
print("The marks after updatemarks() is called as seen from outside the function:",markslist)

