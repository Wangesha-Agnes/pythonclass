def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(29))  # Output: True
print(is_prime(33))  # Output: False

# Write a program for managing bank accounts. the program should require the user's account number and output the balance and transaction history of the user. Additionally, the user should be allowed to deposit and withdraw
        
def multiply_values(list1, list2):
    result_list = []
    for value1, value2 in zip(list1, list2):
       result_list.append(value1 * value2)
    print(result_list)
    
class Bank:
   def __init__(self, account_number, current_balance):
       self.account_number = account_number
       self.balance = current_balance
       self.transactions = []

   def check_balance(self):
        print(self.balance)

   def deposit(self, new_amount):
       self.balance += new_amount
       self.transactions.append(f"{new_amount} has been deposited to the account.")
       print(f"{new_amount} has been deposited in your account.")

   def withdraw(self, new_amount):
        if new_amount <= self.balance:
            self.balance -= new_amount
            self.transactions.append(f"{new_amount} has been withdrawn.")
            return f"{new_amount} has been withdrawn successfully and the new balance is {self.balance}"
        else:
            print("Insufficient amount. Please top up.")
   def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)


account = Bank(account_number="abcd123456789", current_balance=20000)
account.deposit(3500)
account.withdraw(5000)
account.display_transaction_history()
