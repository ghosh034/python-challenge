#import dependencies
import os
import csv

#file location
csvpath = os.path.join('..','PyPoll','election_data.csv')

#declare variables 
totalvotes = 0 
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0
khan_percentage = []
correy_percentage = []
li_percentage = []
otooley_percentage= []

#open csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
#iterate through rows and calculate totalvotes
    for row in csvreader:
        totalvotes += 1
#count candidate votes 
        if row[2] == "Khan": 
            khanvotes +=1
        elif row[2] == "Correy":
            correyvotes +=1
        elif row[2] == "Li": 
            livotes +=1
        elif row[2] == "O'Tooley":
            otooleyvotes +=1

#create lists for candidates and candidatevotes
candidates = ["Khan", "Correy", "Li","O'Tooley"]
candidatevotes = [khanvotes, correyvotes, livotes, otooleyvotes]

#zip candidate and candidatevotes and create dictionary to hold zipped list
mydict = dict(zip(candidates, candidatevotes))
winner = max(mydict, key=mydict.get)

#calculating candidate % votes
khan_percentage.append(round(khanvotes/totalvotes * 100,5))
correy_percentage.append(round(correyvotes/totalvotes * 100,5))
li_percentage.append(round(livotes/totalvotes * 100,5))
otooley_percentage.append(round(otooleyvotes/totalvotes * 100,5))

#print results to terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {totalvotes}")
print(f"----------------------------")
print(f"Khan: {khan_percentage:}% ({khanvotes})")
print(f"Correy: {correy_percentage:}% ({correyvotes})")
print(f"Li: {li_percentage:}% ({livotes})")
print(f"O'Tooley: {otooley_percentage:}% ({otooleyvotes})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#create output file
output_file = os.path.join('..', 'PyPoll', 'analysissummary.txt')
with open(output_file,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"------------------------")
    file.write("\n")
    file.write(f"Total Votes: {totalvotes}")
    file.write("\n")
    file.write(f"-------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percentage:}% ({khanvotes})")
    file.write("\n")
    file.write(f"Correy: {correy_percentage:}% ({correyvotes})")
    file.write("\n")
    file.write(f"Li: {li_percentage:}% ({livotes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percentage:}% ({otooleyvotes})")
    file.write("\n")
    file.write(f"------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"------------------------")

