import os
import csv

pyBank_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_pl = 0
greatest_increase = 0
greatest_decrease = 0
previous_total = 0
current_total = 0
difference = 0
sum_of_difference = 0
listaverage = 0.0
name = "Brandon Daniels"

# Go to file then open it and read the CSV
with open(pyBank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    csv_header = next(csvreader)
    #print(csv_header)
    #Select the first row
    #firstrow = next(csvreader)
    #grab prev value from first row
    #previous_total = int(firstrow[1])

    for row in csvreader:  
        total_months = total_months + 1
        total_pl = total_pl + int(row[1])
        current_total = int(row[1])
        if total_months > 1:
            difference = current_total - previous_total
            #print(difference)
            sum_of_difference = sum_of_difference + difference
            #print(sum_of_difference)
            if difference > greatest_increase:
                greatest_increase = difference
                max_month = row[0]
            if difference < greatest_decrease:
                greatest_decrease = difference
                min_month = row[0]
        #else:
        previous_total = current_total
        
        
listaverage = round(sum_of_difference / (total_months - 1), 2)
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_pl}")
print(f"Average Change:(${listaverage})")
print(f"Greatest Increase in Profits: {max_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})\n")
print("By: " + name + " Spr 2020 Class")