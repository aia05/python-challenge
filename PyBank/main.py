import os
import csv

budget_data = os.path.join(".", "Resources" , "budget_data.csv")

totalMonths = 0
profitLoss = 0
value = 0
change = 0
dates = []
profits = []

with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    first_row = next(csvreader)
    totalMonths += 1
    profitLoss += int(first_row[1])
    value = int(first_row[1])

    for row in csvreader:
        dates.append(row[0])
        
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        totalMonths += 1
        profitLoss = profitLoss + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Avg Profit/Losses
    avg_change = sum(profits)/len(profits)
    

#Output
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: ${str(profitLoss)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(totalMonths)}")
line4 = str(f"Total: ${str(profitLoss)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
