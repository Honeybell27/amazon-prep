def transaction_log(func):
    def wrapper(*args, **kwargs):
        print("🔄Transaction starting...")
        result = func(*args, **kwargs)
        print(f"✅ Result: {result}")
        print("✅Transaction completed.")
        return result
    return wrapper


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @transaction_log
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"✅{amount} deposited successfully"

        else:
            return "Deposit amount must be positive"

    @transaction_log
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return f"{amount} withdrawn successfully."

    def __str__(self):
        return f"Owner: {self.owner} | Balance: {self.balance}"


user1 = BankAccount("Mrs Clara", 500)

user1.withdraw(500)
print(user1)