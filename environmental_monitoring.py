#Algorithm
Start the program.
Display a menu to select air-quality or water-quality analysis.
Accept environmental readings as nested lists.
Validate the readings and threshold values.
Calculate the average, minimum, and maximum readings for each monitoring location.
Compare each reading with the supplied thresholds.
Classify each observation as Good, Moderate, or Poor.
Display the results in a structured format.
Stop the program.
#Flowchart
       +----------------------+
       |        START         |
       +----------------------+
                  |
                  v
       +----------------------+
       | Select Air or Water  |
       | Quality Monitoring   |
       +----------------------+
                  |
                  v
       +----------------------+
       | Enter Nested Lists   |
       | and Threshold Values |
       +----------------------+
                  |
                  v
       +----------------------+
       | Validate Input Data  |
       +----------------------+
                  |
                  v
       +----------------------+
       | Calculate Average,   |
       | Minimum and Maximum  |
       +----------------------+
                  |
                  v
       +----------------------+
       | Classify Readings    |
       | Using Thresholds     |
       +----------------------+
                  |
                  v
       +----------------------+
       | Display Analysis     |
       | Results              |
       +----------------------+
                  |
                  v
       +----------------------+
       |         END          |
       +----------------------+
#code
# Environmental Monitoring Data Analyzer

def classify_reading(value, threshold1, threshold2):
    if value <= threshold1:
        return "Good"
    elif value <= threshold2:
        return "Moderate"
    else:
        return "Poor"


def analyze_data(data, threshold1, threshold2):
    for i, readings in enumerate(data, start=1):
        average = sum(readings) / len(readings)
        minimum = min(readings)
        maximum = max(readings)

        print(f"\nMonitoring Location {i}")
        print("Readings:", readings)
        print(f"Average: {average:.2f}")
        print(f"Minimum: {minimum:.2f}")
        print(f"Maximum: {maximum:.2f}")

        for j, value in enumerate(readings, start=1):
            category = classify_reading(
                value, threshold1, threshold2
            )
            print(f"Reading {j}: {value} - {category}")


def main():
    print("ENVIRONMENTAL MONITORING DATA ANALYZER")
    print("1. Air Quality")
    print("2. Water Quality")

    try:
        choice = int(input("Select monitoring type (1 or 2): "))

        if choice not in (1, 2):
            print("Invalid choice!")
            return

        locations = int(input("Enter number of locations: "))

        if locations <= 0:
            print("Number of locations must be positive.")
            return

        data = []

        for i in range(locations):
            count = int(input(
                f"Enter number of readings for location {i + 1}: "
            ))

            if count <= 0:
                print("Each location must have at least one reading.")
                return

            readings = []

            for j in range(count):
                value = float(input(f"Enter reading {j + 1}: "))

                if value < 0:
                    print("Readings cannot be negative.")
                    return

                readings.append(value)

            data.append(readings)

        threshold1 = float(input("Enter first threshold: "))
        threshold2 = float(input("Enter second threshold: "))

        if threshold1 < 0 or threshold2 <= threshold1:
            print("Invalid thresholds!")
            print("Thresholds must be non-negative and increasing.")
            return

        if choice == 1:
            print("\nAIR QUALITY ANALYSIS")
        else:
            print("\nWATER QUALITY ANALYSIS")

        analyze_data(data, threshold1, threshold2)

    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()
    #sample output
    ENVIRONMENTAL MONITORING DATA ANALYZER
1. Air Quality
2. Water Quality
Select monitoring type (1 or 2): 1
Enter number of locations: 2

Enter number of readings for location 1: 3
Enter reading 1: 25
Enter reading 2: 40
Enter reading 3: 65

Enter number of readings for location 2: 3
Enter reading 1: 30
Enter reading 2: 55
Enter reading 3: 80

Enter first threshold: 35
Enter second threshold: 60

AIR QUALITY ANALYSIS

Monitoring Location 1
Readings: [25.0, 40.0, 65.0]
Average: 43.33
Minimum: 25.00
Maximum: 65.00
Reading 1: 25.0 - Good
Reading 2: 40.0 - Moderate
Reading 3: 65.0 - Poor

Monitoring Location 2
Readings: [30.0, 55.0, 80.0]
Average: 55.00
Minimum: 30.00
Maximum: 80.00
Reading 1: 30.0 - Good
Reading 2: 55.0 - Moderate
Reading 3: 80.0 - Poor