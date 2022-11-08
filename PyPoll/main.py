#import the functions needed 
import os
import csv
from collections import Counter

#import the data file
vote_data = os.path.join('Resources','election_data.csv')

#create empty lists 
Vote_id = []
candidate = []

#Set the count to 0
count = 0 

#read the file 
with open(vote_data,'r') as csvfile:
    reader = csv.DictReader(csvfile)

    #Read all rows and append the list values
    for row in reader:
        count = count + 1
        Vote_id.append(row['Ballot ID'])
        candidate.append(row['Candidate'])

    #calculate the number of votes
    v = (len(Vote_id))
    print("Total votes:  " + str(v))

    #Get Candiate Names 
    names = set(candidate)
    list(names)
    
    cand_name = []

    for i in names:
        cand_name.append(i)
    
    
    a = cand_name[0]
    b = cand_name[1]
    c = cand_name [2]
    

    a_vote = (candidate.count(a))
    b_vote = (candidate.count(b))
    c_vote = (candidate.count(c))

    a_per = (a_vote/v)*100
    b_per = (b_vote/v)*100
    c_per = (c_vote/v)*100
    
    a_fin = (round(a_per,3))
    b_fin = (round(b_per,3))
    c_fin = (round(c_per,3))

    print(str(a) + ": " + str(a_fin) + "% (" + str(a_vote) + ")")
    print(str(b) + ": " + str(b_fin) + "% (" + str(b_vote) + ")")
    print(str(c) + ": " + str(c_fin) + "% (" + str(c_vote) + ")")
    




