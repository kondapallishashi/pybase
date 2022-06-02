#String join(seq) joins the elements in the sequence using the seperator in the original string.
str='*'
charSeq=('p','y','t','h','o','n')
print("Joining characters in a sequence str.join(charSeq) : ",str.join(charSeq))
str="   This is a sample string  "
#The ljust(width,[fillchar]) returns the left justified string of length width. 
#If width is less than len(str), original string is returned
#The default fill character is space.
print("str.ljust(40):", str.ljust(40))
print("str.ljust(40):", str.ljust(40,'*'))
print("str.ljust(40):", str.ljust(10,'*'))

#rjust() returns the right justified string of width original length with space as the default character.
print("str.rjust(40):", str.rjust(40))
print("str.rjust(40):", str.rjust(40,'*'))
print("str.rjust(40):", str.rjust(10,'*'))

#lstrip() strips the characters from the beginning or the left side. Default is space.
print("Strip the spaces from the string using str.lstrip():", str.lstrip())
str1="*****This is a sample string*********"
print("Strip the '*' from the string using str1.lstrip('*'):", str1.lstrip('*'))

#rstrip() strips the characters from the ending or the right side. Default is space.
print("Strip the spaces from the string using str.rstrip():", str.rstrip())
print("Strip the '*' from the string using str1.rstrip('*'):", str1.rstrip('*'))

#strip() strips the characters from the beginning and ending of the string. Default is space.

print("Strip the spaces from the string using str.strip():", str.strip())
print("Strip the '*' from the string using str1.strip('*'):", str1.strip('*'))

#str.zfill(width) fills the width by padding the string with zeros on the left.
str="This is a sample string"
print("Fill the width on the left of string with 0s using str.zfill(40)", str.zfill(40))

str="PYTHON IS POWERFUL"
print("The letters of a string can be converted to lowercase using str.lower() : ", str.lower())
str="python is powerful"
print("The letters of a string can be converted to uppercase using str.upper(): ", str.upper())
str = "ThiS is A mIXed CasE sEnteNce"
print("The case of each character in a string can be swapped using str.swapcase(): ", str.swapcase())
#maketrans() and translate() methods.
intab="aeiou"
outtab="12345"
#The maketrans() method maps each character in the intab with corresponding characater in outtab and returns a traslate table.
#The returned translate table is used as input for translate() function
translateTable=str.maketrans(intab,outtab)
#print(translateTable)
str="This is a sample string output"
print("Translate the string applying translateTable: str.translate(translateTable): ", str.translate(translateTable))
#All the above steps can be consolidated into a single statement.
print(str.translate(str.maketrans(intab,outtab)))

str = "!@ this is a sample string that 1s u5ed to LEARN string methods() in 24 hours !@"
print("Replace 'th' with '**' using str.replace('th','**'):\n", str.replace('th','**'))
print("Replace 2 occurances of 'th' with '**' using str.replace('th','**',2):\n", str.replace('th','**',2))

#split() returns a list of all the words in the string, using sep as the separator, default is spaces
print ("str.split( ):",str.split( ))
print ("str.split('i'):",str.split('i'))
print ("str.split('i',40):",str.split('i',40))
print ("str.split('s',20):",str.split('s',20))

#splitlines(num=str.count('\n')) returns all the lines in a string optionally including the linebreaks.
str2="This is\n a sample \n string that can \n be used to \ncount lines"
print("str2.splitlines():", str2.splitlines())
print("str2.splitlines(num=str2.count('\\n')):", str2.splitlines(str2.count('\\n')))



