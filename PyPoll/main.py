#import the functions needed 
import os
import csv
from collections import Counter

#import the data file
vote_data = os.path.join('Resources','election_data.csv')

#create empty lists 
Vote_id = []
candidate = []

#read the file 
with open(vote_data,'r') as csvfile:
    reader = csv.reader(csvfile)

    #Store the headers
    headers = next(reader,None)
    
    column= {}

    for h in headers:
        column[h] = []

    
    for row in reader:
        for h, e in zip(headers, row):
            column[h].append(e)

    #create empty lists 
    Vote_id = column['Ballot ID']
    candidate = column['Candidate']

    
    #Print the headers
    print("\nElection Results \n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

    #calculate the number of votes
    v = (len(Vote_id))
    print("Total votes:  " + str(v))

    #print the break line
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

    #Get Candiate Names
    names = set(candidate)
    list(names)

    #Store canditate names in a list
    cand_name = []

    for i in names:
        cand_name.append(i)
    
    cand_name = sorted(cand_name)

    #Seperate candiate names out 
    a = cand_name[0]
    b = cand_name[1]
    c = cand_name [2]
    
    #Count the votes for each candiate
    a_vote = (candidate.count(a))
    b_vote = (candidate.count(b))
    c_vote = (candidate.count(c))

    #Change the votes into a percentage
    a_per = (a_vote/v)*100
    b_per = (b_vote/v)*100
    c_per = (c_vote/v)*100
    
    #Round the Votes to 3dp
    a_fin = (round(a_per,3))
    b_fin = (round(b_per,3))
    c_fin = (round(c_per,3))

    #Print the Voting totals and headers
    print(str(a) + ": " + str(a_fin) + "% (" + str(a_vote) + ")\n")
    print(str(b) + ": " + str(b_fin) + "% (" + str(b_vote) + ")\n")
    print(str(c) + ": " + str(c_fin) + "% (" + str(c_vote) + ")")

    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
    
    #Make lists to find the max 
    namelist = (a, b, c)
    votelist = (a_vote, b_vote, c_vote)

    #Identify the highest vote 
    max_vote = max(votelist)
    max_index = votelist.index(max_vote)
    w = (namelist[max_index])

    #Print the winner and seperator
    print("Winner:  " + w)
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

    #Output the results to a txt file 
    output = os.path.join('analysis','Analysis.txt')
    with open(output,'w',newline= "\n") as text_file:
        text_file.write("Election Results \n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
        text_file.write("\nTotal votes:  " + str(v))
        text_file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
        text_file.write(str(a) + ": " + str(a_fin) + "% (" + str(a_vote) + ")\n\n")
        text_file.write(str(b) + ": " + str(b_fin) + "% (" + str(b_vote) + ")\n\n")
        text_file.write(str(c) + ": " + str(c_fin) + "% (" + str(c_vote) + ")")
        text_file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
        text_file.write("Winner:  " + w)
        text_file.write("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")





