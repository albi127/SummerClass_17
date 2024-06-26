# -*- coding: utf-8 -*-
"""COVID19.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1800a0dQx2WLIy7-ZulMHAblsvy5xsHrf
"""

import statistics

def main():
    # List of newly infected patients per day
    infection_numbers = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412,
                         1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

    # Calculate statistics
    minimum = min(infection_numbers)
    maximum = max(infection_numbers)
    range_val = maximum - minimum
    mean = statistics.mean(infection_numbers)
    median = statistics.median(infection_numbers)
    variance = statistics.variance(infection_numbers)
    std_dev = statistics.stdev(infection_numbers)

    # Print the results
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Range: {range_val}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")

if __name__ == "__main__":
    main()