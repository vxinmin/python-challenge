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
        month = 0 
        next_month = 0
        profit_losses_list = []
        date_list = []

        month = month + 1
        net_amount += int(row[1])
        profit_losses_list.append(int(row[1]))
        date_list.append(row[0])
        average_change = (profit_losses_list[-1] - profit_losses_list[0])/(month)
        maximum = max(profit_losses_list)
        minimum = min(profit_losses_list)
        
        max_reference = profit_losses_list.index(maximum)
        min_reference = profit_losses_list.index(minimum)
        
print ("Financial Analysis")
print ("----------------------------------------")
print (f"Total Months: {month}")
print (f"Total : {net_amount}")
print (f"Average Change: {average_change}")
print (f'Greaster Increase In Profits: {date_list[max_reference]} (${maximum})')
print (f'Greaster Decrease In Profits: {date_list[min_reference]} (${minimum})')
