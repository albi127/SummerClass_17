# -*- coding: utf-8 -*-
"""gallons.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DOx3DPo8MAlv78FzAq6XPCMWV9giwM7A
"""

print ('heloo world')

def main():
    total_miles = 0
    total_gallons = 0
    count = 0

    while True:
        gallons = float(input("Enter the gallons used (-1 to end): "))
        if gallons == -1:
            break
        miles = float(input("Enter the miles driven: "))

        miles_per_gallon = miles / gallons
        print(f"The miles/gallons for this tank was {miles_per_gallon:.6f}")

        total_miles += miles
        total_gallons += gallons
        count += 1

    if count != 0:
        overall_average = total_miles / total_gallons
        print(f"The overall average miles/gallons was {overall_average:.6f}")
    else:
        print("No data to calculate overall average miles/gallons.")

if __name__ == "__main__":
    main()
2