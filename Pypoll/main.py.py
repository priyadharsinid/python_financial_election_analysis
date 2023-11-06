#os module allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

#path to csvfile
csvpath=os.path.join("Resources","election_data.csv")

#path to textfile
analysis = os.path.join("Analysis", "Election_Analysis.txt")

#set variable for total votes,list of candidate ,total number/percentage of votes for each candidate
totalvote=0
cand_Vote=0
cand_percent=0

canditate=[]
ballot=[]
unique_list=[]
cand_Vote_list=[]
cand_percent_list=[]

#Read using csv module
with open(csvpath,encoding='UTF-8') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
   csv_header = next(csvreader)
 
   print(f'CSV Header: {csv_header}\n')

   for row in csvreader:
     totalvote+=1
     ballot.append(row[0])
     canditate.append(row[2])

     #Find list of candidate
   for name in canditate:   
      if name not in unique_list:
        unique_list.append(name)

     #Find total number of votes for each candidate
   for i in range(len(unique_list)):
      for name in canditate:
        if name == unique_list[i]:
         cand_Vote+=1
      cand_Vote_list.append(cand_Vote) 
      cand_Vote=0

     #Find percentage of votes fore each candidate    

for i in range(len(cand_Vote_list)):
    cand_percent=(cand_Vote_list[i]/totalvote)*100
    cand_percent_list.append(cand_percent)
    cand_percent=0

print("Election Results\n")
print("---------------------------\n")
print(f'Total Votes: {totalvote}\n')
print("--------------------------\n")
for i in range (len(unique_list)):
   print(f'{unique_list[i]}: {cand_percent_list[i]:.3f}% ({cand_Vote_list[i]})\n')
print("--------------------------\n")
print(f'Winner: {unique_list[(cand_Vote_list.index(max(cand_Vote_list)))]}\n')
print("-------------------------")

with open(analysis,"w") as textfile:
   textfile.write("Election Results\n\n")
   textfile.write("------------------------\n\n")
   textfile.write(f'Total Votes:{totalvote}\n\n')
   textfile.write("-------------------------\n\n")
   for i in range (len(unique_list)):
     textfile.write(f'{unique_list[i]}: {cand_percent_list[i]:.3f}% ({cand_Vote_list[i]})\n\n') 
   textfile.write("-----------------------\n\n")
   textfile.write(f'Winner: {unique_list[(cand_Vote_list.index(max(cand_Vote_list)))]}\n\n')
   textfile.write("-------------------------")

  