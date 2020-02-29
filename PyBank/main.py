import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path,'budget_data.csv')
txtpath = os.path.join(dir_path,'output.txt')

months = 0
p_l_t = 0
prev_p_l = 867884
p_l_min = 0
p_l_max = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        months += 1
        p_l_t += int(row[1])
        delta = int(row[1]) - prev_p_l
        prev_p_l = int(row[1])
        if delta >= p_l_max:
            p_l_max = delta
            max_mon = row[0]
        elif delta <= p_l_min:
            p_l_min = delta
            min_mon = row[0]
        else:
            continue
    
    avg_delta = round(delta / (months - 1),2)
    output = ["Financial Analysis\n","----------------------------\n",f"Total Months: {months}\n",f"Total: ${p_l_t}\n",f"Average  Change: ${avg_delta}\n",f"Greatest Increase in Profits: {max_mon} (${p_l_max})\n",f"Greatest Decrease in Profits: {min_mon} (${p_l_min})\n"]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${p_l_t}")
    print(f"Average  Change: ${avg_delta}")
    print(f"Greatest Increase in Profits: {max_mon} (${p_l_max})")
    print(f"Greatest Decrease in Profits: {min_mon} (${p_l_min})")

txtfile = open(txtpath,'w')
txtfile.writelines(output) 
txtfile.close()
