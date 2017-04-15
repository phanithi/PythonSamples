'''
Created on Apr 1, 2017

@author: Phanithi
'''

class Dictionary(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print('In Default constructor..')
        
        
    def runDictionarySol(self):    
        
        # Using keys and indexing, grab the 'hello' from the following dictionaries: d = {'simple_key':'hello'}
        d = {'simple_key':'hello'}
        print(d['simple_key'])
        
        d = {}
        d['simple_key'] = 'hello'
        print(d['simple_key']) #If no key present in dictionary then KeyError will be thrown.
        
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


d = Dictionary()
d.runDictionarySol()

