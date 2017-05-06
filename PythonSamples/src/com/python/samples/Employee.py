'''
Created on Apr 1, 2017

To practice different rules on CLASS. Chapter 8-54

@author: Phanithi
'''

class Employee(object):
    '''
     @ Solutions for the Objects and Data Structures Assessment Test
    '''
    # Class Variables. These variable can be accessed using class name. e., Employee.organization
    organization= "IBM"
    location = "Hyderabad"
    
    '''
    Rules:
    1.__init__ is not mandatory to have in class. If not present default constructor will be provided by runtime. 
    2. Object can be created like Employee(). If presented, then arguments should match with the __init__. e.g., Employee('Nagaraju', 'IBM') 
        and Employee() can't be called any more. 
    3. There can be only one __init_ method in any given class. Either with default__init__(self)  or argument __init__(self, name).
    '''
    def __init__(self, empName, org):
        empName = empName
        
        # This will not set org value to the organization declared at class level. Instead it will be set to local variable of __init__.
        organization = org;
        
        #To set class variable use class name
        Employee.organization = org
        Employee.name = empName
        
    def getEmpId(self):
        return self.empId
    
    #class variables (accessible using class name) and attributes (accessible using self) can be created in methods
    # Any variable can't be accessed directly unless they are declared as arguments. They can be accessed only using class name or self.
    def setEmpId(self, empId):
        
        self.empId = empId
        Employee.empId = "1234"
        print("Employee Id set to : "+empId)
        
    
        
d= Employee("Nagaraju", "Sears")

print(Employee.organization)
print(Employee.name);

d.setEmpId("08285G")
print(d.empId)
print(d.getEmpId())
print(Employee.organization)
print('Added by phanithi')
