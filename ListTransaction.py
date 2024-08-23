


class ListTransaction:
    '''A class that preserves the original list passed in if things go bad
        and an exception occurs while trying to modify the member list
    '''
    
    #called right after the instance is created with __new__
    #sets the arguments passed into the constructor
    def __init__(self, thelist):
        print('__init__ was called')
        self.thelist = thelist #sets the instance's thelist property to what
        #was passed in

    def __enter__(self):
        #called when 'with obj' executes
        #indicates that a new context is being entered
        #in this case, 'this' is the context manager object
        
        print('__enter__ was called')
        self.workingcopy = list(self.thelist) #creates a copy of thelist
        return self.workingcopy #returns the working copy of thelist

    def __exit__(self, type, value, traceback):
        #called when flow of execution leaves the context block
        #if there was no exception that caused the context block to be exited, then
        #type, value and traceback are set to None
        #if there was an exception then appropriate values are passed as arguments
        print('__exit__ was called')
        if type is None: #no exception, set thelist to be the modifications made to the working copy. #all is good
            self.thelist[:] = self.workingcopy#[:] is slicy for "a slice that's really the whole thing"
        return False #lets the exception propogate if there is one

items = [1, 2, 3]
with ListTransaction(items) as working: #'as working', causes the return value of __enter__ to be
    #placed in the variable 'working'. So working is the workingcopy list
    working.append(4) #appends to workingcopy -- see above.
    working.append(5)
    #here control flow exits the managed context
    #that causes __exit__ to be called
        #if no exceptions then thelist (a variable which points to the same thing items points to)
            #is loaded with the context of workingcopy - changes preserved
        #if an exception caused the exit from the managed context
            #then the copy of workingcopy into thelist never happens. items does not get modified       

print(items) #appending of 4 and 5 works

try:
    with ListTransaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError('I see a bad thing') #this will prevent the self.thelist[:] assignment above from happening
    #thelist (and items) will go unmodified
except RuntimeError:
    pass #do nothing to handle the exception

print(items) #no appending of 6 and 7




    
