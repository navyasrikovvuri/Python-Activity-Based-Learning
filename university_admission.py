#Algorithm
Start the program.
Input the number of applicants.
For each applicant, enter:
Applicant name
Mathematics marks
Physics marks
Chemistry marks
Computer Science marks
Calculate the aggregate percentage of each applicant.
Check subject eligibility:
Mathematics ≥ 50
Physics ≥ 50
Chemistry ≥ 50
Computer Science ≥ 50
Check whether the aggregate percentage is at least 60%.
If all eligibility conditions are satisfied, mark the applicant as eligible; otherwise, mark the applicant as ineligible.
Sort eligible applicants according to:
Highest aggregate percentage first.
Highest Mathematics marks in case of a tie.
Highest Computer Science marks if both aggregate and Mathematics marks are equal.
Assign ranks to eligible applicants.
Display the ranked list of eligible applicants and the list of rejected applicants.
Stop the program.
#flowchart
              ┌─────────────────┐
              │      START      │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Input Number of │
              │ Applicants      │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Enter Applicant │
              │ Details and Marks│
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Calculate       │
              │ Aggregate       │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Check Subject   │
              │ Eligibility     │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Aggregate >= 60%│
              │ and Subjects OK?│
              └────┬────────┬───┘
                   │        │
                  Yes       No
                   │        │
           ┌───────▼────┐ ┌─▼────────────┐
           │ Add to     │ │ Add to       │
           │ Eligible   │ │ Rejected List│
           └───────┬────┘ └─────┬────────┘
                   │            │
                   └─────┬──────┘
                         │
                ┌────────▼────────┐
                │ More Applicants?│
                └────┬────────┬───┘
                     │        │
                    Yes       No
                     │        │
                Repeat Input  │
                              │
                    ┌─────────▼────────┐
                    │ Sort Eligible    │
                    │ Applicants       │
                    └─────────┬────────┘
                              │
                    ┌─────────▼────────┐
                    │ Assign Ranks and │
                    │ Display Results  │
                    └─────────┬────────┘
                              │
                    ┌─────────▼────────┐
                    │      STOP        │
                    └──────────────────┘
#code
# University Admission Decision Engine

applicants = []
eligible = []
rejected = []

# Course eligibility criteria
MIN_SUBJECT_MARK = 50
MIN_AGGREGATE = 60

print("===== UNIVERSITY ADMISSION SYSTEM =====")

n = int(input("Enter number of applicants: "))

# Collect applicant details
for i in range(n):
    print(f"\nApplicant {i + 1}")

    name = input("Enter applicant name: ")

    maths = float(input("Enter Mathematics marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    computer = float(input("Enter Computer Science marks: "))

    # Validate marks
    marks = [maths, physics, chemistry, computer]

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Invalid marks! Marks must be between 0 and 100.")
        continue

    # Calculate aggregate percentage
    aggregate = sum(marks) / len(marks)

    # Store applicant details
    applicant = {
        "name": name,
        "maths": maths,
        "physics": physics,
        "chemistry": chemistry,
        "computer": computer,
        "aggregate": aggregate
    }

    applicants.append(applicant)

    # Check subject eligibility
    subject_eligible = all(
        mark >= MIN_SUBJECT_MARK for mark in marks
    )

    # Check aggregate eligibility
    aggregate_eligible = aggregate >= MIN_AGGREGATE

    if subject_eligible and aggregate_eligible:
        eligible.append(applicant)
    else:
        rejected.append(applicant)

# Rank eligible applicants
eligible.sort(
    key=lambda x: (
        x["aggregate"],
        x["maths"],
        x["computer"]
    ),
    reverse=True
)

# Display ranked eligible applicants
print("\n========== ELIGIBLE APPLICANTS ==========")

if eligible:
    print(f"{'Rank':<8}{'Name':<15}{'Aggregate':<15}"
          f"{'Maths':<10}{'Computer':<10}")

    print("-" * 58)

    for rank, applicant in enumerate(eligible, start=1):
        print(
            f"{rank:<8}"
            f"{applicant['name']:<15}"
            f"{applicant['aggregate']:<15.2f}"
            f"{applicant['maths']:<10.2f}"
            f"{applicant['computer']:<10.2f}"
        )
else:
    print("No eligible applicants.")

# Display rejected applicants
print("\n========== INELIGIBLE APPLICANTS ==========")

if rejected:
    for applicant in rejected:
        print(
            f"{applicant['name']} - "
            f"Aggregate: {applicant['aggregate']:.2f}%"
        )
else:
    print("No rejected applicants.")

print("\nTotal Applicants :", len(applicants))
print("Eligible         :", len(eligible))
print("Ineligible       :", len(rejected))

print("==========================================")
#sample output
===== UNIVERSITY ADMISSION SYSTEM =====
Enter number of applicants: 4

Applicant 1
Enter applicant name: Rahul
Enter Mathematics marks: 85
Enter Physics marks: 80
Enter Chemistry marks: 75
Enter Computer Science marks: 90

Applicant 2
Enter applicant name: Priya
Enter Mathematics marks: 95
Enter Physics marks: 90
Enter Chemistry marks: 92
Enter Computer Science marks: 96

Applicant 3
Enter applicant name: Arjun
Enter Mathematics marks: 60
Enter Physics marks: 55
Enter Chemistry marks: 58
Enter Computer Science marks: 65

Applicant 4
Enter applicant name: Sneha
Enter Mathematics marks: 45
Enter Physics marks: 80
Enter Chemistry marks: 75
Enter Computer Science marks: 85

========== ELIGIBLE APPLICANTS ==========
Rank    Name           Aggregate      Maths     Computer
----------------------------------------------------------
1       Priya          93.25          95.00     96.00
2       Rahul          82.50          85.00     90.00
3       Arjun          59.50          60.00     65.00

========== INELIGIBLE APPLICANTS ==========
Sneha - Aggregate: 71.25%

Total Applicants : 4
Eligible         : 3
Ineligible       : 1
==========================================