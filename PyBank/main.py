#* Your task is to create a Python script that analyzes the records to calculate each of the following:

# * The total number of months included in the dataset
# * The net total amount of "Profit/Losses" over the entire period

 # * The average of the changes in "Profit/Losses" over the entire period

 # * The greatest increase in profits (date and amount) over the entire period

  #* The greatest decrease in losses (date and amount) over the entire period

#*# As an example, your analysis should look similar to the one below:

 # ```text
 # Financial Analysis

  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
 # Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#########################################################################
import os
import csv

os.chdir(os.path.dirname(__file__)) #changed directory to source of this main.py file  
csvpath = os.path.join('..', '..', 'PyBank', 'Resources', 'budget_data.csv')
#csvpath = '..\..\Resources\budget_data.csv'
#print(csvpath) #WORKS
profit_loss_total = 0 
#/Homework 3; Python/python-challenge/PyBank/main.py
#/Homework 3; Python/PyBank/Resources/budget_data.csv
#file = '../../PyBank/Resources/budget_data.csv'

with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  next(csvreader)
  profit_loss_total = []
  date = []
  profit_loss_change = []
  profit_loss = []
  #avg_profit_loss_change = []

  #print(csvreader)  #why doesnt this work?
  csv_list = list(csv.reader(csvfile))
  #print(csv_list)  ###WORKS
  ##next(csvreader)  ####WORKS
  #next(csv_list)csv
  ##profit_loss_total = sum(int(row[1]) for row in csvreader)  ###WORKS
  ##print("Profit/Loss Total: " + str(profit_loss_total))  ###WORKS
   
  for row in csv_list:
    #print(row[1])
    profit_loss.append(int(row[1], 10))
    date.append(row[0])
  sum_profit_loss = sum(profit_loss)
  #print(profit_loss)
  
  #print("Profit/Loss : $" + sum[profit_loss])

 
  for x in range(1,len(profit_loss)):
    profit_loss_change.append(profit_loss[x]- profit_loss[x-1])
    
    avg_profit_loss_change = sum(profit_loss_change)/len(profit_loss_change)
    max_profit_loss_change = max(profit_loss_change)
    min_profit_loss_change = min(profit_loss_change)
    max_profit_loss_change_date = str(date[profit_loss_change.index(max(profit_loss_change))])
    min_profit_loss_change_date = str(date[profit_loss_change.index(min(profit_loss_change))])

###############################################################
  print("Financial Analysis")
  print("------------------")
  print(f"Total Months: {len(list(csv_list))}")  ###WORKS 
  print(f"Total Amount: {sum_profit_loss}")
  print(f"Average Change:  {round(avg_profit_loss_change,2)}")  
  print(f"Greatest increase in profits: {max_profit_loss_change_date} ${max_profit_loss_change}")
  print(f"Greatest decrease in profits: {min_profit_loss_change_date} ${min_profit_loss_change}")

printedmonths = len(list(csv_list))
sum_profit_loss

output = (
  f"Total Months: {printedmonths}/n" 
  f"Total Amount: {sum_profit_loss}/n"
  f"Average Change: {round(avg_profit_loss_change,2)}/n"
  f"Greatest increase in profits: {max_profit_loss_change_date} ${max_profit_loss_change}/n"
  f"Greatest decrease in profits: {min_profit_loss_change_date} ${min_profit_loss_change}/n"

)

output_path = os.path.join("pybank.txt")
with open(output_path, 'w') as txt_file:
  txt_file.write(output)
  
