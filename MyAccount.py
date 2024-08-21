"""
    Class that will hold Account details of a customer.
        Account should have ability to store Account Number, Type, Customer Name, Balance.
            Ex: 101, Savings, Ram, 5000

        Business Rules -
            1. At time of opening of any account, the minimum deposit amount should be 1000.
            2. At any point in time, the balance of a SAVINGS account should be at least 500,
                                     the balance of a CHECKING account should be at least 250
            3. The operations allowed should be -
                (a) Deposit
                (b) Withdrawal
                (c) Get latest status
"""

class OpeningAccountDepositAmountException(Exception):
    pass

class DepositAmountNotIntegerException(Exception):
    pass

class DepositAmountValueNotValid(Exception):
    pass

class MinimumBalanceException(Exception):
    pass

class Account:

    def __init__(self, acno, cname, atype, amount):
        if amount < 1000:
           raise OpeningAccountDepositAmountException("You need to have at least 1000 deposited at time of opening of any bank account") 
            
        self.account_number = acno
        self.customer_name = cname
        self.account_type = atype
        self.balance = amount

    def __str__(self):
        print()
        return "Account Number is: " + str(self.account_number) + "\nCustomer Name is: " + self.customer_name + "\nAccount Type is: " + self.account_type + "\nBalance is: " + str(self.balance)
        print()
    
    def deposit(self, amount):
        if not type(amount) is int:
            raise DepositAmountNotIntegerException("You need to provide an Integer as amount for Deposit/Withdrawal")
        
        if amount <= 0:
            raise DepositAmountValueNotValid("You need to deposit/withdraw at least 1$")
            
        self.balance += amount

    def withdrawal(self, amount):
        if not type(amount) is int:
            raise DepositAmountNotIntegerException("You need to provide an Integer as amount for Deposit/Withdrawal")
        
        if amount <= 0:
            raise DepositAmountValueNotValid("You need to deposit/withdraw at least 1$")
            
        if self.account_type == "Savings":
            if self.balance - amount < 500:
                raise MinimumBalanceException("You need to maintain at least 500 for Savings Account")
        elif self.account_type == "Checking":
            if self.balance - amount < 250:
                raise MinimumBalanceException("You need to maintain at least 250 for Checking Account")

        self.balance -= amount

















