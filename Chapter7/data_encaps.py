class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def __repr__(self):
        return f'Account({self.owner!r}, {self._balance!r})'

    def deposit(self, amount):
        self._balance += amount #by naming convention, balance is "private"

    def withdraw(self, amount):
        self._balance -= amount #by naming convention, balance is "private"

    def inquiry(self):
        return self._balance
    

#acc = Account("Fred Fright", 1111.11)
#print(acc)

#but nothing prevents this. it's all naming conventions
#print(acc._balance)
#print()
#print()

#mangling via 2 underscores, private names in a superclass can't be
#overwritten by identical names in a child class
class A:
    def __init__(self):
        self.__x = 3

    def __spam(self):
        print('A.__spam', self.__x)

    def bar(self):
        print('bar in A')
        self.__spam()

class B(A):
    def __init__(self):
        A.__init__(self)
        self.__x = 37

    def __spam(self):    
        print('B.__spam', self.__x) 

    def grok(self):
        print('grok in B')
        self.__spam()

    """
    in python3 repl .....
    bee.bar() prints A.__spam 3
    line 45 should have overwritten A's __spam() so that line 38
    would have called the new overwritten __spam() at line 45
    But ... __spam() at line 33 got mangled to _A__spam()
    So the override at line 45 never happened
    Line 45 creates a unique __spam() method for B (eventually mangled to _B__spam())
    So ... in bee.bar(), line 38 calls line 33 and that function uses the not overwritten (mangled) __x variable in A
    To print out "A.__spam() 3" 

    """