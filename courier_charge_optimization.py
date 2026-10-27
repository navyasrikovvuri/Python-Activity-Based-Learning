#Algorithm
Start the program.
Input the parcel's weight, length, width, and height.
Input the delivery distance zone: Local, Regional, or National.
Input the delivery urgency: Standard, Express, or Same-Day.
Input declared restrictions, such as fragile items or prohibited materials.
Validate the parcel dimensions and weight.

Calculate the volumetric weight using the formula:

Volumetric Weight = (Length × Width × Height) / 5000

Determine the chargeable weight by selecting the greater of actual weight and volumetric weight.
Calculate delivery charges based on the distance zone and chargeable weight.
Add the urgency surcharge and fragile-handling fee, if applicable.
Check the eligibility requirements for each courier service.
Compare the charges of eligible services.
Select the eligible service with the lowest delivery charge.
Display the charges, service eligibility, and recommended courier service.
Stop the program.
#flowchart
             ┌───────────────────┐
             │       START       │
             └─────────┬─────────┘
                       │
             ┌─────────▼─────────┐
             │ Input Parcel      │
             │ Weight and Size   │
             └─────────┬─────────┘
                       │
             ┌─────────▼─────────┐
             │ Input Zone,       │
             │ Urgency, and      │
             │ Restrictions      │
             └─────────┬─────────┘
                       │
             ┌─────────▼─────────┐
             │ Validate Inputs   │
             └─────────┬─────────┘
                       │
                 ┌─────▼─────┐
                 │ Valid?    │
                 └──┬─────┬──┘
                  No│     │Yes
             ┌──────▼─┐   │
             │ Display│   │
             │ Error  │   │
             └────┬───┘   │
                  │   ┌───▼──────────┐
                  │   │ Calculate    │
                  │   │ Chargeable   │
                  │   │ Weight       │
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Calculate    │
                  │   │ Service Fees │
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Check Service│
                  │   │ Eligibility  │
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Compare      │
                  │   │ Eligible Fees│
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Select Lowest│
                  │   │ Eligible Fee │
                  │   └───┬──────────┘
                  │       │
                  │   ┌───▼──────────┐
                  │   │ Display      │
                  │   │ Results      │
                  │   └───┬──────────┘
                  │       │
                  └───┬───┘
                      │
             ┌────────▼────────┐
             │      STOP       │
             └─────────────────┘
#code
# Courier Charge Optimization

import math

print("===== COURIER CHARGE OPTIMIZATION =====")

# Input parcel details
try:
    weight = float(input("Enter parcel weight (kg): "))
    length = float(input("Enter length (cm): "))
    width = float(input("Enter width (cm): "))
    height = float(input("Enter height (cm): "))

    if min(weight, length, width, height) <= 0:
        print("Error: Weight and dimensions must be positive.")
        raise SystemExit

    zone = input(
        "Enter delivery zone (local/regional/national): "
    ).lower().strip()

    urgency = input(
        "Enter urgency (standard/express/same-day): "
    ).lower().strip()

    fragile = input(
        "Is the parcel fragile? (yes/no): "
    ).lower().strip()

    prohibited = input(
        "Does it contain prohibited materials? (yes/no): "
    ).lower().strip()

    # Validate choices
    if zone not in ["local", "regional", "national"]:
        print("Invalid delivery zone.")
        raise SystemExit

    if urgency not
           #sample output
           ===== COURIER CHARGE OPTIMIZATION =====
Enter parcel weight (kg): 5
Enter length (cm): 30
Enter width (cm): 20
Enter height (cm): 15
Enter delivery zone (local/regional/national): regional
Enter urgency (standard/express/same-day): express
Is the parcel fragile? (yes/no): yes
Does it contain prohibited materials? (yes/no): no

========== COURIER SERVICE COMPARISON ==========

Actual Weight       : 5.00 kg
Volumetric Weight   : 1.80 kg
Chargeable Weight   : 5.00 kg
Delivery Zone       : Regional
Urgency             : Express
Fragile Handling    : Yes

------------------------------------------------
Service             Estimated Charge   Status
------------------------------------------------
Standard Courier    Rs. 250.00         Eligible
Express Courier     Rs. 350.00         Eligible
Premium Courier     Rs. 450.00         Eligible
------------------------------------------------

Recommended Service : Standard Courier
Minimum Charge      : Rs. 250.00
================================================