#import dependencies
import os
import csv

#file location
csvpath = os.path.join('..','PyBank','budget_data.csv')

#create empty lists for variables
totalmonths = []
totalprofit = []
monthlyprofitchange = []

#open csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
#iterate through rows and append totalmonths and totalprofits to lists   
    for row in csvreader:
        totalmonths.append(row[0])
        totalprofit.append(int(row[1]))
#calculate diference for monthlyprofitchange and append to list
    for i in range(len(totalprofit)-1):
        monthlyprofitchange.append(totalprofit[i+1]-totalprofit[i])
#calculate greatestincrease and greatestdecrease and corresponding months
greatestincrease = max(monthlyprofitchange)
greatestdecrease = min(monthlyprofitchange)
greatestincreasemonth = monthlyprofitchange.index(max(monthlyprofitchange)) + 1
greatestdecreasemonth = monthlyprofitchange.index(min(monthlyprofitchange)) + 1

#print statements to terminal
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {len(totalmonths)}")
print(f"Total: ${sum(totalprofit)}")
print(f"Average Change: {round(sum(monthlyprofitchange)/len(monthlyprofitchange),2)}")
print(f"Greatest Increase in Profits: {totalmonths[greatestincreasemonth]} (${(str(greatestincrease))})")
print(f"Greatest Decrease in Profits: {totalmonths[greatestdecreasemonth]} (${(str(greatestdecrease))})")

#create output textfile
output_file = os.path.join('..', 'PyBank', 'analysissummary.txt')

with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(totalmonths)}")
    file.write("\n")
    file.write(f"Total: ${sum(totalprofit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthlyprofitchange)/len(monthlyprofitchange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {totalmonths[greatestincreasemonth]} (${(str(greatestincrease))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {totalmonths[greatestdecreasemonth]} (${(str(greatestdecrease))})")
