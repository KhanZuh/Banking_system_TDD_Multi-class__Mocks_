class Account:
    def __init__(self, deposit):
        if deposit <= 0:
            raise ValueError("Account balance cannot be zero")
        self.balance = deposit

