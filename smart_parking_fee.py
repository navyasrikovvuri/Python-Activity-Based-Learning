#Algorithm
Start the program.
Input the vehicle category: Two-wheeler, Car, or Heavy vehicle.
Input the entry time and exit time in HH:MM format.
Validate the time inputs to ensure they contain valid hours and minutes.
Calculate the total parking duration. If the exit time is earlier than the entry time, assume the vehicle exited the following day.
Calculate the parking duration in hours and round up to the next whole hour.
Apply parking rates according to the vehicle category:
Two-wheeler: ₹10 per hour
Car: ₹20 per hour
Heavy vehicle: ₹40 per hour
Check whether overnight parking occurred and apply the overnight surcharge, if applicable.
Apply the daily parking limit according to the vehicle category.
Check penalty conditions, such as exceeding the allowed parking duration.
Calculate the final parking fee.
Display the vehicle category, parking duration, overnight status, penalty, and total fee.
Stop the prgram
#flowchart
              ┌─────────────────┐
              │      START      │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Input Vehicle   │
              │ Category         │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Input Entry and │
              │ Exit Times      │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Validate Time   │
              │ Inputs          │
              └────────┬────────┘
                       │
                 ┌─────▼─────┐
                 │ Valid?    │
                 └──┬─────┬──┘
                  No│     │Yes
             ┌──────▼─┐   │
             │ Display│   │
             │ Error  │   │
             └────┬───┘   │
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Calculate    │
                  │   │ Duration     │
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Calculate    │
                  │   │ Basic Fee    │
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Apply Daily  │
                  │   │ Parking Limit│
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Check        │
                  │   │ Overnight Fee│
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Check Penalty│
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Calculate    │
                  │   │ Total Fee    │
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Display Bill │
                  │   └───┬──────────┘
                  │       │
                  └───┬───┘
                      │
              ┌───────▼────────┐
              │      STOP      │
              └────────────────┘
#code
# Smart Parking Fee Management

import math
from datetime import datetime, timedelta

print("===== SMART PARKING FEE MANAGEMENT =====")

# Vehicle category rates
rates = {
    "two-wheeler": 10,
    "car": 20,
    "heavy vehicle": 40
}

daily_limits = {
    "two-wheeler": 100,
    "car": 300,
    "heavy vehicle": 500
}

OVERNIGHT_FEE = 50
PENALTY = 200

# Input vehicle category
vehicle = input(
    "Enter vehicle category (two-wheeler/car/heavy vehicle): "
).lower().strip()

if vehicle not in rates:
    print("Invalid vehicle category!")

else:
    try:
        # Input and validate entry and exit times
        entry_input = input("Enter entry time (HH:MM): ")
        exit_input = input("Enter exit time (HH:MM): ")

        entry = datetime.strptime(entry_input, "%H:%M")
        exit_time = datetime.strptime(exit_input, "%H:%M")

        # Convert times to minutes after midnight
        entry_minutes = entry.hour * 60 + entry.minute
        exit_minutes = exit_time.hour * 60 + exit_time.minute

        # Calculate duration, considering overnight parking
        if exit_minutes < entry_minutes:
            exit_minutes += 24 * 60

        duration_minutes = exit_minutes - entry_minutes

        if duration_minutes == 0:
            print("Invalid parking duration: Entry and exit times are equal.")

        else:
            # Calculate duration in hours
            duration_hours = duration_minutes / 60
            charged_hours = math.ceil(duration_hours)

            # Calculate basic fee
            basic_fee = charged_hours * rates[vehicle]

            # Apply daily maximum
            basic_fee = min(basic_fee, daily_limits[vehicle])

            # Check overnight parking
            overnight = exit_minutes >= 24 * 60
            overnight_fee = OVERNIGHT_FEE if overnight else 0

            # Check penalty conditions
            penalty = PENALTY if duration_minutes > 24 * 60 else 0

            # Calculate final fee
            total_fee = basic_fee + overnight_fee + penalty

            # Display parking receipt
            print("\n========== PARKING RECEIPT ==========")
            print(f"Vehicle Category : {vehicle.title()}")
            print(f"Entry Time       : {entry_input}")
            print(f"Exit Time        : {exit_input}")
            print(f"Parking Duration : {duration_hours:.2f} hours")
            print(f"Charged Hours    : {charged_hours}")
            print(f"Hourly Rate      : Rs. {rates[vehicle]:.2f}")
            print(f"Basic Parking Fee: Rs. {basic_fee:.2f}")
            print(f"Overnight Fee    : Rs. {overnight_fee:.2f}")
            print(f"Penalty          : Rs. {penalty:.2f}")
            print("-------------------------------------")
            print(f"TOTAL PARKING FEE: Rs. {total_fee:.2f}")
            print("=====================================")

    except ValueError:
        print("Invalid time format! Please use HH:MM (00:00 to 23:59).")
        #sample output
        ===== SMART PARKING FEE MANAGEMENT =====
Enter vehicle category (two-wheeler/car/heavy vehicle): car
Enter entry time (HH:MM): 20:00
Enter exit time (HH:MM): 02:30

========== PARKING RECEIPT ==========
Vehicle Category : Car
Entry Time       : 20:00
Exit Time        : 02:30
Parking Duration : 6.50 hours
Charged Hours    : 7
Hourly Rate      : Rs. 20.00
Basic Parking Fee: Rs. 140.00
Overnight Fee    : Rs. 50.00
Penalty          : Rs. 0.00
-------------------------------------
TOTAL PARKING FEE: Rs. 190.00
=====================================
===== SMART PARKING FEE MANAGEMENT =====
Enter vehicle category (two-wheeler/car/heavy vehicle): car
Enter entry time (HH:MM): 25:30
Enter exit time (HH:MM): 18:00
Invalid time format! Please use HH:MM (00:00 to 23:59).