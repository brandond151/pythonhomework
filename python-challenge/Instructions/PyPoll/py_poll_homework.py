#import os and csv files
import os
import csv

#set path
pyPoll_csv = os.path.join('Resources', 'election_data.csv')

#initialize variables
candidates = []
number_of_votes = 0
count_of_votes = []

#open the file
with open(pyPoll_csv,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header
    csv_header = next(csvreader)

    #go line by line and process each vote
    for row in csvreader:

        #add to total number of votes
        number_of_votes = number_of_votes + 1

        #candidate voted for
        candidate = row[2]

        #if candidate has other votes then add to vote tally
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            count_of_votes[candidate_index] = count_of_votes[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates.append(candidate)
            count_of_votes.append(1)

percentages = []
max_votes = count_of_votes[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = count_of_votes[count]/number_of_votes*100
    percentages.append(vote_percentage)
    if count_of_votes[count] > max_votes:
        max_votes = count_of_votes[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {number_of_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({count_of_votes[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")