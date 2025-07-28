from datetime import datetime


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @staticmethod
    def view_transaction_history():
        try:
            with open("transaction_log.txt", "r") as file:
                print("\n📄 Transaction History:")
                print(file.read())

        except FileNotFoundError:
            print("No transaction  history found")

    @staticmethod
    def log_transaction(message):
        try:
            with open("transaction_log.txt", "a") as file:
                time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"[{time_stamp}] {message}\n")

        except Exception as e:
            print(f"Logging failed: {e}")

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            error_msg = "Amount must be a number."
            self.log_transaction(f"{self.owner} failed: {error_msg}")
            return error_msg

        if amount > 0:
            self.balance += amount
            message = f"{self.owner} deposited:{amount}. New balance:{self.balance}"
            print(message)
            self.log_transaction(message)
            return f"✅{amount} deposited successfully"

        else:
            error_msg = "Deposit amount must be positive."
            self.log_transaction(f"{self.owner} failed to deposit: {error_msg}")
            return error_msg

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            error_msg = "Amount must be a number."
            self.log_transaction(f"{self.owner} failed: {error_msg}")
            return error_msg

        if amount <= 0:
            error_msg = f"Withdrawal amount must be positive"
            self.log_transaction(f"{self.owner} failed to withdraw: {error_msg}")
            return error_msg

        if amount > self.balance:
            error_msg = f"Insufficient Balance"
            self.log_transaction(f"{self.owner} failed to withdraw: {error_msg}")
            return error_msg

        else:
            self.balance -= amount
            message = f"{self.owner} withdrew {amount}. New balance: {self.balance}"
            print(message)
            self.log_transaction(message)
            return f"✅{amount} withdrawn successfully."

    def __str__(self):
        return f"Owner: {self.owner} | Balance: {self.balance}"


user1 = BankAccount("Mrs Clara", 500)


print(user1.deposit(200))
print(user1.withdraw(100))
print(user1.withdraw(1000))