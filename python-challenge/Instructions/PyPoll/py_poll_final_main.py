import os
import csv

pyPoll_csv = os.path.join('Resources', "election_data.csv")

student_name = "Brandon Daniels"
candidates = []
number_of_votes = 0
count_of_votes = []
percentages = []
max_index = 0

# Go to file then open it and read the CSV
with open(pyPoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        
    #skip the header
    csv_header = next(csvreader)

    #Count each vote line by line...
    for line in csvreader:

        #Then we need to add a vote to the total number
        number_of_votes = (number_of_votes + 1)
        #candidate voted for
        candidate = line[2]
        #Add to total for each tally, per canidate
        if candidate in candidates:
            index_of_canidates = candidates.index(candidate)
            count_of_votes[index_of_canidates] = count_of_votes[index_of_canidates] + 1
        #else create new spot in list for the canidate
        else:
            candidates.append(candidate)
            count_of_votes.append(1)

max_votes = count_of_votes[0]
#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = round(float(count_of_votes[count]/number_of_votes)*100, 3)
    percentages.append(vote_percentage)
    if count_of_votes[count] > max_votes:
        max_votes = count_of_votes[count]
        max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {number_of_votes}")
print("--------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}00% ({count_of_votes[count]})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")
print(f"By: {student_name} :)")