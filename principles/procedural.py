# Banking system simiulation
"""
    A CRUD app to manage user accounts . Entities: accounts, storage Operations: withdraw, deposit, check_balance etc
"""
accounts = [
    {"name": "Dan", "number": "123456789", "balance": 0},
    {"name": "John", "number": "987654321", "balance": 0},
    {"name": "Jane", "number": "555555555", "balance": 0},
    {"name": "Bob", "number": "111111111", "balance": 0},
    {"name": "Alice", "number": "222222222", "balance": 0},
    
]

while True:
    cmd = input("A for all, Q for quit, C for Create account, R for Retrieving account info, U for update and D for deleting: ")
    if cmd == "Q":
        print("Bye...ATM is stopping")
        break
    elif cmd == "A":
        print(accounts)

    elif cmd == "C":
        new_acct_name = input("Enter account name: ")
        new_acct_number = input("Enter account number: ")
        new_acct = {"name": new_acct_name, "number": new_acct_number, "balance": 0}
        accounts.append(new_acct)
        print("Account created successfully")
    elif cmd == "R":
        acct_number = input("Enter account number: ")
        for account in accounts:
            number_in_storage = account["number"]
            if number_in_storage == acct_number:
                print(account)
                break
        else:
            print("Account not found")
    




        










