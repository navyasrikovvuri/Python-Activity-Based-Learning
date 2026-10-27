#Algorithm
1.Start the program.
2.Input the venue, equipment, catering, transport, and certificate costs.
3.Input the expected number of participants.
4.Input the sponsorship amount and registration fee per participant.
5.Calculate the total event cost by adding all expenses.
6.Calculate the cost per participant by dividing the total cost by the number of participants.
7.Calculate the total registration revenue.
8.Calculate the total available funds by adding registration revenue and sponsorship.
9.Determine the sponsorship shortfall if the sponsorship amount is less than the total event cost.
10.Calculate the minimum registration count required to break even after considering sponsorship.
11.Display the total expenses, participant contribution, sponsorship shortfall, and break-even registration count.
12.Stop the program.
#FLOW CHART
             ┌───────────────┐
             │     START     │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │ Input Event   │
             │ Expenses      │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │ Input Number  │
             │ of Participants│
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │ Input Sponsor │
             │ and Fee       │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │ Calculate     │
             │ Total Cost    │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │ Calculate     │
             │ Revenue       │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │ Calculate     │
             │ Funding Gap   │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │ Calculate     │
             │ Break-Even    │
             │ Participants  │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │ Display Event │
             │ Budget Report │
             └───────┬───────┘
                     │
             ┌───────▼───────┐
             │     STOP      │
             └───────────────┘
#python code
# Campus Event Financial Planning

import math

print("=== CAMPUS EVENT FINANCIAL PLANNING ===")

# Input event expenses
venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificates = float(input("Enter certificate cost: Rs. "))

# Input participant and funding details
participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))
registration_fee = float(input("Enter registration fee per participant: Rs. "))

# Calculate total event cost
total_cost = venue + equipment + catering + transport + certificates

# Calculate participant contributions
registration_revenue = participants * registration_fee

# Calculate total available funds
total_funds = registration_revenue + sponsorship

# Calculate cost per participant
if participants > 0:
    cost_per_participant = total_cost / participants
else:
    cost_per_participant = 0

# Calculate sponsorship shortfall
sponsorship_shortfall = max(0, total_cost - sponsorship)

# Calculate minimum participants required to break even
if registration_fee > 0:
    remaining_cost = max(0, total_cost - sponsorship)
    break_even_participants = math.ceil(
        remaining_cost / registration_fee
    )
else:
    break_even_participants = 0

# Calculate financial surplus or deficit
balance = total_funds - total_cost

print("\n========== EVENT BUDGET REPORT ==========")

print(f"Venue Cost              : Rs. {venue:.2f}")
print(f"Equipment Cost          : Rs. {equipment:.2f}")
print(f"Catering Cost           : Rs. {catering:.2f}")
print(f"Transport Cost          : Rs. {transport:.2f}")
print(f"Certificate Cost        : Rs. {certificates:.2f}")

print("-----------------------------------------")
print(f"Total Event Cost        : Rs. {total_cost:.2f}")
print(f"Cost Per Participant    : Rs. {cost_per_participant:.2f}")
print(f"Registration Revenue    : Rs. {registration_revenue:.2f}")
print(f"Sponsorship Amount      : Rs. {sponsorship:.2f}")
print(f"Total Available Funds   : Rs. {total_funds:.2f}")
print(f"Sponsorship Shortfall   : Rs. {sponsorship_shortfall:.2f}")
print(f"Break-Even Participants : {break_even_participants}")

if balance > 0:
    print(f"Financial Surplus       : Rs. {balance:.2f}")
elif balance < 0:
    print(f"Financial Deficit       : Rs. {abs(balance):.2f}")
else:
    print("Financial Status        : Break-even")

print("=========================================")
#sample output
=== CAMPUS EVENT FINANCIAL PLANNING ===
Enter venue cost: Rs. 10000
Enter equipment cost: Rs. 5000
Enter catering cost: Rs. 15000
Enter transport cost: Rs. 5000
Enter certificate cost: Rs. 2000
Enter expected number of participants: 100
Enter sponsorship amount: Rs. 10000
Enter registration fee per participant: Rs. 300

========== EVENT BUDGET REPORT ==========

Venue Cost              : Rs. 10000.00
Equipment Cost          : Rs. 5000.00
Catering Cost           : Rs. 15000.00
Transport Cost          : Rs. 5000.00
Certificate Cost        : Rs. 2000.00
-----------------------------------------
Total Event Cost        : Rs. 37000.00
Cost Per Participant    : Rs. 370.00
Registration Revenue    : Rs. 30000.00
Sponsorship Amount      : Rs. 10000.00
Total Available Funds   : Rs. 40000.00
Sponsorship Shortfall   : Rs. 27000.00
Break-Even Participants : 90
Financial Surplus       : Rs. 3000.00
=========================================