'''
Created on Apr 1, 2017

@author: Phanithi
'''

class String(object):
    '''
    classdocs
    '''


    def __init__(self, s):
        print("In constructor..")
        self.s = s
        
         
    #--- ******** String problems ********* ----------   
    def runStringSol(self, s):
        
        # Given the string 'hello' give an index command that returns 'e'. Use the code below:
        print(s[1])
        
        #Reverse the string 'hello' using indexing:
        print(s[::-1])
        
        #Given the string hello, give two methods of producing the letter 'o' using indexing.
        print(s[4]+':'+s[-1])
        

string = String('hello')
string.runStringSol(string.s);