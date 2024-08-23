import random

class StandardPolicy:#a class with only static methods that require no instance, no self variable
    #called by doing StandardPolicy.deposit(account, amount) or similar
    @staticmethod
    def deposit(account, amount):
        account.balance += amount

    @staticmethod
    def withdraw(account, amount):
        account.balance -= amount

    @staticmethod
    def inquiry(account):
        return account.balance
    
class EvilPolicy(StandardPolicy):#inherits from Standard Policy and overrides method definitions, not class methods this time
    #and has its own data, set in the constructor
    def __init__(self, deposit_factor, inquiry_factor):
        self.deposit_factor = deposit_factor
        self.inquiry_factor = inquiry_factor

    def deposit(self, account, amount):
        account.balance += self.deposit_factor * amount#messes with the deposit 

    def inquiry(self, account):
        if random.randint(0,4) == 1:#return a random integer from 0 to 4, if it equals 1 .....
            return self.inquiry_factor * account.balance#lie about the balance
        else:
            return account.balance
        
class Account:
    def __init__(self, owner, balance, *, policy=StandardPolicy):#has a keyword only parameter that defaults to StandardPolicy
        self.owner = owner
        self.balance = balance
        self.policy = policy#policy is flexible, can be passed in to the constructor to change it as needed

    def __repr__(self):
        return f'Account({self.policy}, {self.owner!r}, {self.balance!r})'
        
    def deposit(self, amount):
        self.policy.deposit(self, amount)#use the policy's static methods

    def withdraw(self, amount):
        self.policy.withdraw(self, amount)

    def inquiry(self):
        return self.policy.inquiry(self)
        
acc = Account('Flexi Bob', 1000.0, policy=EvilPolicy(.95, 1.10))
acc.deposit(111.00)
print(acc)

acc.withdraw(213.00)

i = 0
while i < 30:
    print(acc.inquiry())
    i += 1
