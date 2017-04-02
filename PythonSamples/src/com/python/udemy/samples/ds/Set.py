'''
Created on Apr 1, 2017

@author: Phanithi
'''

class Set(object):
    '''
    classdocs
    '''


    def __init__(self):
        print('In default constructor..')
        
        
    def runSetProbSol(self):
        
        s = set()
        s.add(1)
        s.add('a')
        print(s)
        
        s1 = {1, 'a', '2'}
        print(s1)
      
        l = [1, 5, 2, 1, 7, 8]
        print(set(l))  # set with unique list values with sorting done

s = Set()
s.runSetProbSol()

