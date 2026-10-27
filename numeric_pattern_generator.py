#Algorithm
Start the program.
Ask the user to choose a pattern:
Hollow Diamond
Symmetric Number Pattern
Read the height from the user.
Validate that the height is a positive odd integer for the hollow diamond or a positive integer for the symmetric number pattern.
Generate the selected pattern using nested loops.
Display the pattern with proper spacing.
Stop the program.
#Flowchart
       +------------------+
       |      START       |
       +------------------+
                |
                v
       +------------------+
       | Display Menu     |
       +------------------+
                |
                v
       +------------------+
       | Read Choice and  |
       | Pattern Height   |
       +------------------+
                |
                v
       +------------------+
       | Validate Input   |
       +------------------+
                |
                v
       +------------------+
       | Is Input Valid?  |
       +------------------+
          |           |
         No          Yes
          |           |
          v           v
   +-------------+  +------------------+
   | Display     |  | Generate Selected|
   | Error       |  | Numeric Pattern  |
   +-------------+  +------------------+
          |           |
          |           v
          |    +------------------+
          |    | Display Pattern  |
          |    +------------------+
          |           |
          +-----------+
                      |
                      v
              +---------------+
              |      END      |
              +---------------+
#code
# Advanced Numeric Pattern Generator

def hollow_diamond(height):
    mid = height // 2

    for i in range(height):
        row = i if i <= mid else height - 1 - i
        spaces = mid - row

        print(" " * spaces, end="")

        if row == 0:
            print("1")
        else:
            print("1" + " " * (2 * row - 1) + str(row + 1))


def symmetric_number_pattern(height):
    for i in range(1, height + 1):
        # Print leading spaces
        print(" " * (height - i), end="")

        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end="")

        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()


def main():
    print("===== NUMERIC PATTERN GENERATOR =====")
    print("1. Hollow Diamond")
    print("2. Symmetric Number Pattern")

    try:
        choice = int(input("Enter your choice (1 or 2): "))

        if choice not in (1, 2):
            print("Invalid choice! Please select 1 or 2.")
            return

        height = int(input("Enter pattern height: "))

        if height <= 0:
            print("Invalid height! Height must be positive.")
            return

        if choice == 1:
            if height % 2 == 0:
                print("Invalid height! Hollow diamond requires an odd height.")
                return

            print("\nHollow Diamond Pattern:\n")
            hollow_diamond(height)

        else:
            print("\nSymmetric Number Pattern:\n")
            symmetric_number_pattern(height)

    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == "__main__":
    main()
    #sample output
    ===== NUMERIC PATTERN GENERATOR =====
1. Hollow Diamond
2. Symmetric Number Pattern
Enter your choice (1 or 2): 2
Enter pattern height: 5

Symmetric Number Pattern:

    1
   121
  12321
 1234321
123454321
