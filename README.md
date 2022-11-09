# Week3_python-challenge
PyBank and PyPoll homework challenge

PyBank 
Using the os and csv functions the code imports the budget data csv. It pulls the headers out of the csv file and then creates a list of the dates and profit figures. 
The profit figures are then converted into numbers. The code loops through the lists, subtracting each profit value from the preceding month and storing it in a list. 
These figures are then averaged, and the maximum/minimum values are found. These are then printed in the terminal and outputted to a txt file in the analysis folder. 

PyPoll
Using the os and csv functions the code imports the election data csv. The code then pulls out the headers and loops through the required columns to create lists. 
The length of the list determines the number of votes. The code then loops through the lists to find the unique candidate names and the count function tallies up the number of votes. These are then converted into percentages and rounded to three decimal places 
The max function is used to pull out the winner’s name. These are then printed in the terminal and outputted to a txt file in the analysis folder. 
