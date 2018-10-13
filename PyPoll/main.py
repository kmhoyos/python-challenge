import os
import csv

total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""

# open csv file
election_csv = ("election_data.csv")
with open(election_csv,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

# tally votes
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# calc vote percentage
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

# print out results
print(f"Total Votes: {total_votes}")
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} (Total Votes:{vote_count})")
print(f"Winner: {winner}")


# save print to txt
save_file = "pypoll_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write(f"Total Votes: {total_votes}" + "\n")
    for person, vote_count in candidate_votes.items():
        text.write(f"{person}: {candidate_percentages[person]} ({vote_count})" + "\n")
    text.write(f"Winner: {winner}" + "\n")