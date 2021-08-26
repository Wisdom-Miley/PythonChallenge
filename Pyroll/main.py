import os, csv
from pathlib import Path

# Create variable to the list 
total_votes = 0
candidates = []
votes_Per_Candidates = []

# Set path for file
csvpath = Path("PythonChallenge","Pyroll","election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

# create through the election result in order 

    for row in csvreader:
        total_votes += 1
        if total_votes == 1:
            candidates.append(row[2])
            votes_Per_Candidates.append(1)
        else:
            try:
                icandidate = candidates.index(row[2])
                votes_Per_Candidates[icandidate] += 1
            except:
                candidates.append(row[2])
                votes_Per_Candidates.append(1)
                
                
# print statement in order 
results = []
results.append("Election Results\n-------------------------")
results.append(f"Total Votes: {total_votes}\n-------------------------")

winner = candidates[0]
most_votes = votes_Per_Candidates[0]
for i in range(len(candidates)):
    if votes_Per_Candidates[i] > most_votes:
        winner = candidates[i]
        most_votes = votes_Per_Candidates[i]
    percent = 100 * votes_Per_Candidates[i] / total_votes
    results.append(f"{candidates[i]}: {round(percent,3)} % ({votes_Per_Candidates[i]})")

results.append(f"-------------------------\nWinner: {winner}\n-------------------------")

#print election results in txt 
filename = 'Electtion Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + '\n')
