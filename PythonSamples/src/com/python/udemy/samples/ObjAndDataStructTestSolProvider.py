'''
Created on Apr 1, 2017

@author: Phanithi
'''
from _overlapped import NULL

class DataStructSolProvider(object):
    '''
    classdocs
    '''


    def __init__(self):
        print("In default constructor..")
        
    #--- ******** String problems ********* ----------   
    def runStringSol(self):
        
        # Given the string 'hello' give an index command that returns 'e'. Use the code below:
        s = 'hello'
        print(s[1])
        
        #Reverse the string 'hello' using indexing:
        print(s[::-1])
        
        #Given the string hello, give two methods of producing the letter 'o' using indexing.
        print(s[4]+':'+s[-1])
    
    
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
        
        
    def runDictionarySol(self):    
        
        # Using keys and indexing, grab the 'hello' from the following dictionaries: d = {'simple_key':'hello'}
        d = {'simple_key':'hello'}
        print(d['simple_key'])
        
        d = {}
        d['simple_key'] = 'hello'
        print(d['simple_key'])
        
        d = dict()
        d['simple_key'] = 'hello'
        print(d['simple_key'])
        
        
        #d.keys will retrun list of keys in prior python 3.0. But starting from 3.0 onwards, it will return dict_keys class.
        
        print(list(d.keys())[0]) # Not thread safe
        print(list(d.copy().keys())[0]) # expensive. making copy of dict as there is a possibility of another thread may modify the same dict.
        
        print(list(d.values())[0]) 
        print(d) 
        print(list(d.items()))  #Returns list of tuples

        
        # Grab 'hello'
        d = {'k1':{'k2':'hello'}}
        print(d['k1']['k2'])
        
        # Grab 'hello'
        d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
        print(d['k1'][0]['nest_key'][1][0]) # d has list of dictionary whose value is again list.
        
        # This will be hard and annoying!
        d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
        print(d['k1'][2]['k2'][1]['tough'][2][0])
        
        
        d2 = {'k1':1, 'k2':2, 'k3':3}
        
        #Iterate dict and print keys and values
        for item in d2.keys():   # dict_keys class is iteratable. 
            print('key : '+item)
            print('value: '+str(d2[item])) # cast to string as we are concatinating it to 'value'
        
        
    def runSetProbSol(self):
        
        s = set()
        s.add(1)
        s.add('a')
        print(s)
        
        s1 = {1, 'a', '2'}
        print(s1)
      
        l = [1, 5, 2, 1, 7, 8]
        print(set(l))  # set with unique list values with sorting done
        
        
    
        
dsp = DataStructSolProvider();     

#dsp.runStringSol() #Running string problem solutions

#dsp.runListSol() # Running List prob sol's

#dsp.runDictionarySol()  # Running disctionary prob sol's

dsp.runSetProbSol() # Running list prob sol's

        