#Algorithm
Start the program.
Enter the initial account balance.
Enter the maximum withdrawal limit per transaction.
Enter the number of transactions to process.
For each transaction, select the transaction type: deposit or withdrawal.
If the transaction is a deposit:
Enter the deposit amount.
If the amount is positive, add it to the account balance.
Otherwise, reject the transaction.
If the transaction is a withdrawal:
Enter the withdrawal amount.
Check whether the amount is positive.
Check whether it exceeds the withdrawal limit.
Check whether sufficient balance is available.
If all conditions are satisfied, deduct the amount from the balance.
Otherwise, reject the transaction.
Reject any invalid transaction type.
Record the result of every transaction.
Display the transaction summary, total deposits, total withdrawals, rejected transactions, and final balance.
Stop the program.
# Flowchart
             ┌────────────────┐
             │     START      │
             └────────┬───────┘
                      │
             ┌────────▼───────┐
             │ Enter Initial  │
             │ Balance        │
             └────────┬───────┘
                      │
             ┌────────▼───────┐
             │ Enter Number   │
             │ of Transactions│
             └────────┬───────┘
                      │
             ┌────────▼───────┐
             │ Select Deposit │
             │ or Withdrawal  │
             └────────┬───────┘
                      │
              ┌───────▼────────┐
              │ Deposit or     │
              │ Withdrawal?    │
              └───┬────────┬───┘
                  │        │
             Deposit    Withdrawal
                  │        │
          ┌───────▼───┐ ┌──▼─────────────┐
          │ Amount > 0│ │ Amount > 0 and  │
          │     ?     │ │ Within Limit?   │
          └───┬───┬───┘ └──┬─────────┬───┘
              │   │        │         │
             Yes  No      Yes        No
              │   │        │         │
       ┌──────▼┐ ┌▼──────┐ │    ┌────▼─────┐
       │ Add to│ │Reject │ │    │  Reject  │
       │Balance│ │       │ │    │Transaction│
       └───┬───┘ └──┬────┘ │    └────┬─────┘
           │        │      │         │
           │        │  ┌───▼─────────▼──┐
           │        │  │ Sufficient     │
           │        │  │ Balance?       │
           │        │  └───┬────────┬───┘
           │        │      │        │
           │        │     Yes       No
           │        │      │        │
           │        │  ┌───▼────┐ ┌─▼──────┐
           │        │  │ Deduct │ │ Reject │
           │        │  │ Amount │ │        │
           │        │  └───┬────┘ └─┬──────┘
           └────────┴──────┴────────┘
                            │
                   ┌────────▼────────┐
                   │ More Transactions?│
                   └────┬────────┬───┘
                        │        │
                       Yes       No
                        │        │
                 Repeat Process  │
                                 │
                       ┌─────────▼──────┐
                       │ Display Summary│
                       │ and Final      │
                       │ Balance        │
                       └─────────┬──────┘
                                 │
                       ┌─────────▼──────┐
                       │      STOP      │
                       └────────────────┘
#python code
# ATM Transaction Sequence Simulation

print("===== ATM TRANSACTION SIMULATION =====")

# Input initial balance and withdrawal limit
balance = float(input("Enter initial balance: Rs. "))
withdrawal_limit = float(input("Enter maximum withdrawal limit: Rs. "))
n = int(input("Enter number of transactions: "))

# Initialize transaction counters
total_deposits = 0
total_withdrawals = 0
successful_transactions = 0
rejected_transactions = 0

# Store transaction history
transactions = []

# Process transactions
for i in range(n):
    print(f"\nTransaction {i + 1}")
    transaction_type = input(
        "Enter transaction type (deposit/withdrawal): "
    ).lower()

    amount = float(input("Enter amount: Rs. "))

    if transaction_type == "deposit":
        if amount > 0:
            balance += amount
            total_deposits += amount
            successful_transactions += 1
            status = "Successful"
        else:
            status = "Rejected: Invalid amount"
            rejected_transactions += 1

    elif transaction_type == "withdrawal":
        if amount <= 0:
            status = "Rejected: Invalid amount"
            rejected_transactions += 1

        elif amount > withdrawal_limit:
            status = "Rejected: Exceeds withdrawal limit"
            rejected_transactions += 1

        elif amount > balance:
            status = "Rejected: Insufficient balance"
            rejected_transactions += 1

        else:
            balance -= amount
            total_withdrawals += amount
            successful_transactions += 1
            status = "Successful"

    else:
        status = "Rejected: Invalid transaction type"
        rejected_transactions += 1

    # Record transaction details
    transactions.append(
        (i + 1, transaction_type, amount, status, balance)
    )

    print("Status:", status)
    print(f"Current Balance: Rs. {balance:.2f}")

# Display transaction summary
print("\n========== TRANSACTION SUMMARY ==========")

print(f"{'No.':<5}{'Type':<15}{'Amount':<12}"
      f"{'Status':<40}{'Balance':<12}")

print("-" * 84)

for t in transactions:
    print(f"{t[0]:<5}{t[1]:<15}{t[2]:<12.2f}"
          f"{t[3]:<40}{t[4]:<12.2f}")

print("-" * 84)
print(f"Total Deposits           : Rs. {total_deposits:.2f}")
print(f"Total Withdrawals        : Rs. {total_withdrawals:.2f}")
print(f"Successful Transactions  : {successful_transactions}")
print(f"Rejected Transactions    : {rejected_transactions}")
print(f"Final Account Balance    : Rs. {balance:.2f}")

print("=========================================")
#sample output
===== ATM TRANSACTION SIMULATION =====
Enter initial balance: Rs. 5000
Enter maximum withdrawal limit: Rs. 2000
Enter number of transactions: 5

Transaction 1
Enter transaction type (deposit/withdrawal): deposit
Enter amount: Rs. 1500
Status: Successful
Current Balance: Rs. 6500.00

Transaction 2
Enter transaction type (deposit/withdrawal): withdrawal
Enter amount: Rs. 1000
Status: Successful
Current Balance: Rs. 5500.00

Transaction 3
Enter transaction type (deposit/withdrawal): withdrawal
Enter amount: Rs. 2500
Status: Rejected: Exceeds withdrawal limit
Current Balance: Rs. 5500.00

Transaction 4
Enter transaction type (deposit/withdrawal): withdrawal
Enter amount: Rs. 6000
Status: Rejected: Exceeds withdrawal limit
Current Balance: Rs. 5500.00

Transaction 5
Enter transaction type (deposit/withdrawal): deposit
Enter amount: Rs. 500
Status: Successful
Current Balance: Rs. 6000.00

========== TRANSACTION SUMMARY ==========
No.  Type           Amount      Status                                  Balance
------------------------------------------------------------------------------------
1    deposit        1500.00     Successful                              6500.00
2    withdrawal     1000.00     Successful                              5500.00
3    withdrawal     2500.00     Rejected: Exceeds withdrawal limit      5500.00
4    withdrawal     6000.00     Rejected: Exceeds withdrawal limit      5500.00
5    deposit        500.00      Successful                              6000.00
------------------------------------------------------------------------------------
Total Deposits           : Rs. 2000.00
Total Withdrawals        : Rs. 1000.00
Successful Transactions  : 3
Rejected Transactions    : 2
Final Account Balance    : Rs. 6000.00
=========================================