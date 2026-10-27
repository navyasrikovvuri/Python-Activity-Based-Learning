#Algorithm
Start the program.
Enter the number of library branches.
Enter each branch's name, book demand, and priority.
Enter the total number of available book copies.
Validate the input data.
Sort the branches according to priority, with higher-priority branches served first.
Allocate available copies to each branch without exceeding its demand.
Calculate unmet demand for every branch.
Display the allocation details and remaining stock.
Stop the program.
#flowchart
       +---------------------------+
       |           START           |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Enter Available Book      |
       | Copies and Branch Details |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Validate Input Data       |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Sort Branches by Priority |
       | and Demand                |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Allocate Available Copies |
       | According to Priority     |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Calculate Unmet Demand    |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Display Allocation Report |
       +---------------------------+
                    |
                    v
       +---------------------------+
       |            END            |
       +---------------------------+
#code
# Multi-Criteria Library Resource Distribution

def allocate_books(total_copies, branches):
    # Sort by priority, then higher demand
    branches.sort(key=lambda x: (x["priority"], -x["demand"]))

    remaining = total_copies

    print("\n========== LIBRARY ALLOCATION REPORT ==========")
    print(f"Total Available Copies: {total_copies}")
    print("-" * 75)
    print(f"{'Branch':<18}{'Demand':<12}{'Priority':<12}"
          f"{'Allocated':<12}{'Unmet':<10}")
    print("-" * 75)

    total_allocated = 0
    total_unmet = 0

    for branch in branches:
        allocated = min(branch["demand"], remaining)
        unmet = branch["demand"] - allocated

        remaining -= allocated
        total_allocated += allocated
        total_unmet += unmet

        print(f"{branch['name']:<18}"
              f"{branch['demand']:<12}"
              f"{branch['priority']:<12}"
              f"{allocated:<12}"
              f"{unmet:<10}")

    print("-" * 75)
    print(f"Total Allocated Copies: {total_allocated}")
    print(f"Total Unmet Demand:     {total_unmet}")
    print(f"Remaining Stock:        {remaining}")
    print("=" * 75)


def main():
    print("MULTI-CRITERIA LIBRARY RESOURCE DISTRIBUTION")

    try:
        total_copies = int(input("Enter total available book copies: "))
        number_of_branches = int(input("Enter number of branches: "))

        if total_copies < 0 or number_of_branches <= 0:
            print("Invalid input! Copies must be non-negative, "
                  "and branches must be positive.")
            return

        branches = []
        names = set()

        for i in range(number_of_branches):
            print(f"\nBranch {i + 1}")

            name = input("Enter branch name: ").strip()

            if not name:
                print("Branch name cannot be empty.")
                return

            if name.lower() in names:
                print("Duplicate branch names are not allowed.")
                return

            names.add(name.lower())

            demand = int(input("Enter book demand: "))
            priority = int(input("Enter priority (1=High, 2=Medium, "
                                 "3=Low): "))

            if demand < 0:
                print("Demand cannot be negative.")
                return

            if priority not in (1, 2, 3):
                print("Invalid priority! Enter 1, 2, or 3.")
                return

            branches.append({
                "name": name,
                "demand": demand,
                "priority": priority
            })

        allocate_books(total_copies, branches)

    except ValueError:
        print("Invalid input! Please enter integers where required.")


if __name__ == "__main__":
    main()
    #sample output
    MULTI-CRITERIA LIBRARY RESOURCE DISTRIBUTION
Enter total available book copies: 100
Enter number of branches: 4

Branch 1
Enter branch name: Main Library
Enter book demand: 50
Enter priority (1=High, 2=Medium, 3=Low): 1

Branch 2
Enter branch name: Science Library
Enter book demand: 40
Enter priority (1=High, 2=Medium, 3=Low): 2

Branch 3
Enter branch name: Engineering Library
Enter book demand: 35
Enter priority (1=High, 2=Medium, 3=Low): 1

Branch 4
Enter branch name: Arts Library
Enter book demand: 25
Enter priority (1=High, 2=Medium, 3=Low): 3

========== LIBRARY ALLOCATION REPORT ==========
Total Available Copies: 100
---------------------------------------------------------------------------
Branch            Demand      Priority    Allocated   Unmet
---------------------------------------------------------------------------
Engineering Library35         1           35          0
Main Library      50          1           50          0
Science Library   40          2           15          25
Arts Library      25          3           0           25
---------------------------------------------------------------------------
Total Allocated Copies: 100
Total Unmet Demand:     50
Remaining Stock:        0
===========================================================================