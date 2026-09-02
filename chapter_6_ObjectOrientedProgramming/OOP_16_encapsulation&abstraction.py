# Encapsulation & Abstraction

# Encapsulation in Python is an object-oriented programming (OOP) concept where data (attributes) and methods (functions) are bundled together inside a class, and access to the data is controlled to protect it from unintended interference or misuse.

# It helps in:

# Data hiding (restricting direct access to variables)
# Data integrity (controlling how data is modified)
# Abstraction (hiding internal implementation details)

# ======================================================================================

# 1) Encapsulation :


# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder  # Public attribute
#         self._balance = balance               # Protected attribute
#         self.__pin = "1234"                   # Private attribute

#     # Public method to deposit money
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited ₹{amount}. New balance: ₹{self._balance}")
#         else:
#             print("Deposit amount must be positive.")

#     # Public method to withdraw money (with PIN check)
#     def withdraw(self, amount, pin):
#         if pin == self.__pin:
#             if 0 < amount <= self._balance:
#                 self._balance -= amount
#                 print(f"Withdrew ₹{amount}. Remaining balance: ₹{self._balance}")
#             else:
#                 print("Invalid withdrawal amount.")
#         else:
#             print("Incorrect PIN.")

#     # Getter for balance (read-only access)
#     def get_balance(self):
#         return self._balance


# # Example usage
# account = BankAccount("Alice", 5000)

# # Public access
# print(account.account_holder)  # ✅ Works

# # Protected access (possible but discouraged)
# print(account._balance)        # ⚠️ Works, but not recommended

# # Private access (will fail)
# # print(account.__pin)         # ❌ AttributeError

# # Access private variable via name mangling
# print(account._BankAccount__pin)  # ✅ Works, but breaks encapsulation

# # Using methods
# account.deposit(1500)
# account.withdraw(2000, "1234")
# print("Balance:", account.get_balance())

# ======================================================================================

# 2) Abstraction :
    
# In Python, abstraction is the concept of hiding implementation details and exposing only the essential features to the user.
# It helps in reducing complexity and increasing code reusability.

# Key Points

# Achieved mainly using Abstract Classes and Abstract Methods.
# Abstract classes cannot be instantiated directly.
# Subclasses must implement all abstract methods.
# Implemented using the abc (Abstract Base Class) module.


# Example: Abstraction in Python
# Pythonfrom abc import ABC, abstractmethod

# # Abstract Base Class
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         """Start the vehicle's engine"""
#         pass

#     @abstractmethod
#     def stop_engine(self):
#         """Stop the vehicle's engine"""
#         pass

# # Concrete Class implementing abstract methods
# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started.")

#     def stop_engine(self):
#         print("Car engine stopped.")

# class Bike(Vehicle):
#     def start_engine(self):
#         print("Bike engine started.")

#     def stop_engine(self):
#         print("Bike engine stopped.")

# # Usage
# try:
#     v = Vehicle()  # ❌ Will raise TypeError
# except TypeError as e:
#     print(f"Error: {e}")

# my_car = Car()
# my_car.start_engine()
# my_car.stop_engine()

# my_bike = Bike()
# my_bike.start_engine()
# my_bike.stop_engine()


# Output
# Error: Can't instantiate abstract class Vehicle with abstract methods start_engine, stop_engine
# Car engine started.
# Car engine stopped.
# Bike engine started.
# Bike engine stopped.


# Why Use Abstraction?

# Hides complexity — Users don’t need to know how things work internally.
# Enforces a contract — All subclasses must implement required methods.
# Improves maintainability — Changes in implementation don’t affect the interface.


# ✅ Tip:
# If you only want to hide implementation but not enforce method overriding, you can use private methods (prefix with _ or __) instead of abstract classes.

# If you want, I can also give you a real-world banking system example of abstraction in Python to make it more practical.
# Do you want me to prepare that?
