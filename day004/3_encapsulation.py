"""Examples of private attributes and properties in Python."""

class BankAccount:
    """Keep the balance behind methods instead of exposing it directly."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._account_type = "Savings"  # A single underscore is a convention.
        self.__balance = balance        # Double underscore triggers name mangling.

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")


account = BankAccount("Divya", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(5000)

try:
    print(account.__balance)
except AttributeError as e:
    print("\nCan't access directly:", e)

print("Balance via getter:", account.get_balance())


class Temperature:
    """Expose Celsius through a property so assignments can be checked."""

    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32


temp = Temperature(25)
print(f"\n{temp.celsius}°C = {temp.fahrenheit}°F")

temp.celsius = 30
print(f"Updated: {temp.celsius}°C = {temp.fahrenheit}°F")

try:
    temp.celsius = -300   # triggers validation error
except ValueError as e:
    print("Error:", e)
