'''
Created on Apr 1, 2017

@author: Phanithi
'''
from _overlapped import NULL

class List(object):
    '''
    classdocs
    '''


    def __init__(self):
        print("In default constructor")
        
    
    #--- ******* List Problems ********************
    def runListSol(self):
        
        #Build this list [0,0,0] two separate ways.
        lst1 = [0, 0, NULL] # 0 will be inserted for NULL
        print('updated st list -->')
        print(lst1)
        
        lst2 = [0]*3
        print('2nd list --> ')
        print(lst2)
        
        lst3 = [] #you can also say lst3 = list()
        lst3.append(0)
        lst3.append(0)
        lst3.append(0)
        print('3rd list --> ')
        print(lst3)
        
        #Reassign 'hello' in this nested list to say 'goodbye' item in this list: l = [1,2,[3,4,'hello']]
        l = [1,2,[3,4,'hello']]
        l[2][2] = 'goodbye'
        print(l)
        
        #Sort the list l = [3,4,5,5,6]
        l = [3,4,8,5,6]
        l.sort()
        print('1st sorted list')
        print(l)
        
        l = [3,4,8,5,6]
        print(l)
        
        print('2nd sorted list')
        print(sorted(l))

lst = List()
lst.runListSol()