#import the file
import os, csv
from pathlib import Path

# Create variable to the list 
total_votes = 0
votes_per_candidate = {}

# Set path for csvfile
csvpath = Path("PythonChallenge","Pyroll","election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

    
# create through the election result in order 

   for row in csvreader:
        total_votes += 1
        if row[2] not in votes_per_candidate:
            votes_per_pandidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1
#print the result while using str and suse 3% format the total votes 
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for candidate, votes in votes_per_candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
print("-------------------------") 
winner = max(votes_per_candidate, key=votes_per_candidate.get)
print(file"Winner: {winner}")

# write output file as result in txt 
file = open("Election_results.txt", "w")
file.write("Election Results")
file.write('\n')
file.write("-------------------------")
file.write('\n')
file.write("Total Votes: " + str(total_votes))
file.write('\n')
file.write("-------------------------")
file.write('\n')
for candidate, votes in votes_per_candidate.items():
    file.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    file.write('\n')
file.write("-------------------------") 
file.write('\n')
file.write(f"Winner: {winner}")
file.write("-------------------------") 
file.write('\n')
