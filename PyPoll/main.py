import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path,'election_data.csv')
txtpath = os.path.join(dir_path,'output.txt')

total_votes = 0
results = {"votes":{},"percent":{}}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        if row[2] not in results["votes"]:
            #results["votes"][row[2]] = 1
            #results["percent"][row[2]] = 1
            results["votes"][row[2]] = [1,1]
        else:
            results["votes"][row[2]][0] +=1
            results["votes"][row[2]][1] +=1
            #results["votes"][row[2]] += 1
            #results["percent"][row[2]] += 1
        
winner = max(results["votes"], key=results["votes"].get)
for key in results["percent"]:
    results["percent"][key] = round((results["percent"][key]/total_votes)*100,3)
print(results["votes"])


#output = ["Election Results\n","----------------------------\n",f"Total Votes: {total_votes}\n",f"Total: ${p_l_t}\n",f"Average  Change: ${avg_delta}\n",f"Greatest Increase in Profits: {max_mon} (${p_l_max})\n",f"Greatest Decrease in Profits: {min_mon} (${p_l_min})\n"]
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
#for key in results["percent"]:
   # print(f"{key}: {results["percent"][key]}%")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")   

#txtfile = open(txtpath,'w')
#txtfile.writelines(output) 
#txtfile.close()