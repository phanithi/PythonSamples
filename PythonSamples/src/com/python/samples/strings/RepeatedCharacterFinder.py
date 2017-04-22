'''
Created on Apr 13, 2017

@author: Phanithi
'''

# Find 1st repeated character. duplicate comment
def findRepeatedChar(s):
    print('Inside function : findRepeatedChar()')
    if(len(s) == 1) : return s
    
    st = set()
    for ch in s:
        if (ch in st): 
            return ch 

        else: 
            st.add(ch)

print(findRepeatedChar("Hellooo"))