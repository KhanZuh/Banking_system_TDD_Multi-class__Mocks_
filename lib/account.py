class InsufficientFundsError(Exception): # this is a custom exception - new concept for me - googled it - user defined exception errors - so instead of using the ValueError - "Defining a custom exception, therefore, gives you more granularity. It allows you to proceed in different ways depending on which exact type of error happened in your application." 
    pass

class Account:
    def __init__(self, deposit):
        if deposit <= 0:
            raise ValueError("Account balance cannot be zero")
        self.balance = deposit

