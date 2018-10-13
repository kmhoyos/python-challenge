import os
import csv

month_count = 0
total_rev = 0
this_month_rev = 0
last_month_rev = 0
rev_change = 0
rev_changes = []
months = []

# open csv file
budget_csv = ("budget_data.csv")
with open(budget_csv,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

# monthly changes in revenue
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        this_month_rev = int(row[1])
        total_rev = this_month_rev + total_rev
        if month_count > 1:
            rev_change = this_month_rev - last_month_rev
            rev_changes.append(rev_change)
        last_month_rev = this_month_rev

# monthly results
sum_rev_changes = sum(rev_changes)
average_change = sum_rev_changes / (month_count - 1)
max_change = max(rev_changes)
min_change = min(rev_changes)
max_month_index = rev_changes.index(max_change)
min_month_index = rev_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

# print out results
print(f"Total Months: {month_count}")
print(f"Total Revenue: {total_rev}")
print(f"Average Revenue Change: {average_change}")
print(f"Greatest Rev Increase: {max_month} ({max_change})")
print(f"Greatest Rev Decrease: {min_month} ({min_change})")

# save print to txt
save_file = "pybank_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Revenue: {total_rev}" + "\n")
    text.write(f"Avg Revenue Change: {average_change}" + "\n")
    text.write(f"Greatest Rev Increase: {max_month} ({max_change})" + "\n")
    text.write(f"Greatest Rev Decrease: {min_month} ({min_change})" + "\n")