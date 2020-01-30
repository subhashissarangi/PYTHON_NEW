'''
Created on 29-Jan-2020

@author: SUBHASHIS
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    '''
    public members declarations
    '''
    def publicMembers(self, arg1, arg2):
        self.arg1=arg1
        self.arg2=arg2
     
    '''
    protected members declaration
    '''   
    def protectedMembers(self, arg3, arg4):
        self._arg3=arg3
        self._arg4=arg4
    
    '''
    private members declaration
    '''    
    def privateMembers(self, arg5, arg6):
        self.__arg5=arg5
        self.__arg6=arg6   