import os
import csv
pybank_csv_path = os.path.join("budget_data.csv")

with open(pybank_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
