import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path,'election_data.csv')
txtpath = os.path.join(dir_path,'output.txt')

total_votes = 0
results = {"votes":{}}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        if row[2] not in results["votes"]:
            results["votes"][row[2]] = [1,1]
        else:
            results["votes"][row[2]][0] +=1
            results["votes"][row[2]][1] +=1
        
winner = max(results["votes"], key=results["votes"].get)
for key in results["votes"]:
    results["votes"][key][0] = "{0:.3f}".format((results["votes"][key][0]/total_votes)*100)
result_list = [str(key)+': '+str(results["votes"][key][0])+'% '+'('+str(results["votes"][key][1])+')' for key in results["votes"]]

output = ["Election Results\n","----------------------------\n",f"Total Votes: {total_votes}\n","----------------------------\n"]
output2 = ["----------------------------\n",f"Winner: {winner}\n","----------------------------\n"]
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
[print(str(key)+': '+str(results["votes"][key][0])+'% '+'('+str(results["votes"][key][1])+')') for key in results["votes"]]
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")   

txtfile = open(txtpath,'w')
txtfile.writelines(output)
txtfile.writelines("%s\n" % result for result in result_list) 
txtfile.writelines(output2)
txtfile.close()