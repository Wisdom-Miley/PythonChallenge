import os, csv
from pathlib import Path 

# input the csv file 
input_file = Path("PythonChallenge","Pybank","budget_data.csv")
# Create the variable at the list
months = []
total_revenue = []
monthly_revenue_change = []
 
# Open csv with context manager
with open(input_file,newline="", encoding="utf-8") as budget:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the header 
    header = next(csvreader)  

    # Stored file contents
    for row in csvreader: 

        # append the month to the list 
        months.append(row[0])
        total_revenue.append(int(row[1]))

    # create the revenue to the change 
    for i in range(len(total_revenue)-1):
        
        # take the diffence of profit
        monthly_revenue_change.append(total_revenue[i+1]-total_revenue[i])
        
# added the max and min of the the montly revenue change list
max_increase_value = max(monthly_revenue_change)
max_decrease_value = min(monthly_revenue_change)


#calculator max and min in to monthly revenue 
#use + 1 at the end since month change 
max_increase_month = monthly_revenue_change.index(max(monthly_revenue_change)) + 1
max_decrease_month = monthly_revenue_change.index(min(monthly_revenue_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total_revenue)}")
print(f"Average Change: {round(sum(monthly_revenue_change)/len(monthly_revenue_change),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = Path("PythonChallenge","Pybank","financial analysis.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("financial analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_revenue)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_revenue_change)/len(monthly_revenue_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")



