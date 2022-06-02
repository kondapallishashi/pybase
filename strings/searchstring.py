#This program demonstrates various ways the strings can be searched for specific information
str = "!@ this is a sample string that 1s u5ed to LEARN string methods() in 24 hours !@"
print("The Original String is : \n%s" % str)

#String count() method - counts the occurance of the substring. 
#count(subString, [start],[end])
#default start is 0 and default end is end of the string same as len(string)
#Counts the occurance of substring 'is' from start to end
print("str.count('is') : ", str.count('is'))
#Explicitly mention start and end where the sub string needs to be searched.
print("str.count('th',0,len(str)) : ",str.count('th',0,len(str)))
#Reduce the end size to decrease the count.
print("str.count('th',0,len(str)) : ",str.count('th',0,30))

#string startswith(sub,[start=0],[end=len(str)])
#returns true or false depending on whether the substring exists or not.

print("str.startswith('@!') : ", str.startswith('@!'))
print("str.startswith('!@', 0, len(str)) : ", str.startswith('!@', 0, len(str)))
print("str.startswith('!@', 0,2 ) : ", str.startswith('!@', 0, 2))


#String endswith(sub, [start], [end]) method - returns true if string or substring ends with provided substring.
#default start is 0 and end is len(string)
print("str.endswith('@!') : ", str.endswith('@!'))
print("str.endswith('!@', 0, len(str)) : ", str.endswith('!@', 0, len(str)))
print("str.endswith('!@', 0,2 ) : ", str.endswith('!@', 0, 2))

#String find(str,[start=0],[end=len(str)]) method returns index of sub string if found, -1 if not
print("str.find('is'): ",str.find('is'))
#Prints the first occurance
print("str.find('th'): ",str.find('th'))
print("str.find('th', 20): ",str.find('th',20))

#rfind() returns the index of the substring from the end and -1 if not found.
print("str.rfind('th'): ",str.rfind('th'))
print("str.rfind('th',0,20): ",str.rfind('th',0,20))
print("str.rfind('th',0,40): ",str.rfind('th',0,40))
print("str.rfind('th',20,0): ",str.rfind('th',20,0))

#String index(str,[start=0],[end=len(str)]) is similar to find(). Returns index if sub string is found and throws an exception if not found.
print("str.index('hours'): ",str.index('hours'))
#Throws an exception as figment substring is not found in string str.
#print("str.index('figment'): ",str.index('figment'))

#String rindex(str,[start=0],[end=len(str)]) returns the last index of the sub string if found and -1 if not found
print("str.rindex('th'): ",str.rindex('th'))
print("str.rindex('th',0,20): ",str.rindex('th',0,20))
print("str.rindex('th',0,40): ",str.rindex('th',0,40))
#This statement throws an exception with the error message index not found.
#print("str.rindex('th'): ",str.rindex('th',20,0))






#