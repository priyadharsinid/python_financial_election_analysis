#os module allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

#path to csv
csvpath = os.path.join("Resources", "budget_data.csv")

#path to textfile
analysispath = os.path.join("Analysis", "Financial_Analysis.txt")

#set variable for totalmonths,total amount,averagechange,greatest inc /dec in profit (date and month)
total_months = 0
total_amount = 0
avg_change=0
grt_inc=0
grt_dec=0
grt_inc_month=""
grt_dec_month=""

monthlist=[]
profitloss_list=[]
Change_PL=[]


#Read using csv module
with open(csvpath,encoding='UTF-8') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
   csv_header = next(csvreader)
 
   print(f'CSV Header: {csv_header}\n')

#Read each row of data
   for row in csvreader:
    monthlist.append(row[0])
    profitloss_list.append(row[1])
    total_months+=1
    total_amount+=int(row[1])
   for i in range(len(profitloss_list)-1):
        Change_PL.append(int(profitloss_list[i+1])-int(profitloss_list [i]))

  #Find average change,greatest inc/dec in profits (date and amount)
avg_change=round(sum(Change_PL)/len(Change_PL),2)
grt_inc=max(Change_PL)
grt_dec=min(Change_PL)
grt_inc_month=monthlist[Change_PL.index(grt_inc)+1]
grt_dec_month=monthlist[Change_PL.index(grt_dec)+1]

#print result to terminal
print("Financial Analysis\n")
print("---------------------------\n")
print(f'Total Months: {total_months}\n')
print(f'Total: ${total_amount}\n')
print(f'Average Change: ${avg_change}\n')
print(f'Greatest Increase in Profits: {grt_inc_month} (${grt_inc})\n')
print(f'Greatest Decrease in Profits: {grt_dec_month} (${grt_dec})\n')

#write result to textfile

with open(analysispath,'w') as textfile:
 
    textfile.write("Financial Analysis\n\n")
    textfile.write("--------------------------\n\n")
    textfile.write(f'Total Months: {total_months}\n \n')
    textfile.write(f'Total: ${total_amount}\n \n')
    textfile.write(f'Average Change: ${avg_change}\n \n')
    textfile.write(f'Greatest Increase in Profits: {grt_inc_month} (${grt_inc})\n \n')
    textfile.write(f'Greatest Decrease in Profits: {grt_dec_month} (${grt_dec})\n \n')