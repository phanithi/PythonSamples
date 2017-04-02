'''
Created on Mar 29, 2017

@author: Phanithi
'''
a = 'hello World';
print(a.capitalize()) #(Result: Hello World) --> Return a capitalized version of S, i.e. make the first character have upper case and the rest lower case.

b = "Hello World World hello Hello";
print(b.count("World")) # (Result: 2) --> Returns no. of Occurences of given sub string in the string on which method invokes.

c = "Welcome to "
print(c+a) 

# a[start index: end index] --> Sub string
print(a[:]) # prints entire string 'a'

print(a[2:]); # prints the sub string starting index at 2 to till the end

print(len(a)); # length = 11. String length

print(a[:len(a)-2]) # Result = 'hello Wor'. Prints the sub string from starting to 9 (9 is excluded)

print(a[1:5]) #Result = 'ello' (character at position '1' is included but at 5 is excluded)

# a[start index: end index: increament by]
print(a[::]) # Print whole string.. by default start index=0; end index= length of string; increamented by=1

print(a[2:7:1]) # Prints 'llo Q=W' string increated by 1

print(a[::2]) #Prints 'hloWrd' --> prints every 2nd character starting from 0 index.

print(a[::-1]) #Prints the string in reverse. 

#print(a[15]) # string index out of range.
print(a[-2]); # prints 'l'. String index starts from 0 to 10 (e.g)... 10 to 0 are same as -1 to -10

print(a.find("world")) #Returns -1 if the given substring is not present. If present returns its index.

print(a.upper()) #Prints whole string in UPPER case

print(1/2) # Result= 0.5.  for python 2.7 earlier versions, it ignores the digits after decaimal point.







