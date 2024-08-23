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
    
class EvilPolicy(StandardPolicy):#inherits from Standard Policy and overrides method definitions
    @staticmethod
    def deposit(account, amount):
        account.balance += 0.95 * amount#messes with the deposit 

    @staticmethod
    def inquiry(account):
        if random.randint(0,4) == 1:#return a random integer from 0 to 4, if it equals 1 .....
            return 1.10 * account.balance#lie about the balance
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
        
acc = Account('Bob Bucks', 1000)
print(acc)
print(acc.inquiry())

acc.deposit(211)
print(acc.inquiry())

acc.withdraw(99)
print(acc.inquiry())

bac_acc = Account('Bad Bob Bucks', 1000, policy=EvilPolicy)
print(bac_acc)
print(bac_acc.inquiry())

bac_acc.deposit(211)
print(bac_acc.inquiry())

bac_acc.withdraw(99)
print(bac_acc.inquiry())
