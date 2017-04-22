'''
Created on Apr 13, 2017

@author: Phanithi
'''
from _overlapped import NULL

class MyClass(object):
    '''
    classdocs
    '''

# constructor
    def __init__(self):
        '''
        Constructor
        '''
        
    #Recursive approach    
    def reverse(self, s):
        if (s== NULL or len(s) == 1): return s
        return self.reverse(s[1:])+s[0];
    
mc = MyClass();
print(mc.reverse('Hello'))
print(mc.reverse('Phanithi'))
