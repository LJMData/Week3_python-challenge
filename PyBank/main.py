#Import the fuctions needed 
import os
import csv

#Import the data file 
bank_data = os.path.join('Resources','budget_data.csv')

#Create empty lists 
month =[]
profit =[]

#read the file 
with open(bank_data,'r') as csvfile:
    reader = csv.reader(csvfile)

    #Store the headers
    headers = next(reader,None)
    
    column= {}

    for h in headers:
        column[h] = []

    
    for row in reader:
        for h, e in zip(headers, row):
            column[h].append(e)
    
   
   #Add the values to the lists
    month = column['Date']
    profit = column ['Profit/Losses']
       
    
    #Turn the profit strings into intergers
    profit_num = (int(item) for item in profit)


    #Print out the outputs
    print("\n \n Financial Analysis \n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n \n ")
    print(f"Total Months: " + str(len(month))+ "\n")
    print(f"Total $" + str(sum(profit_num)) + "\n")

    #Get numerical values for each profit and months
    p = [eval(i) for i in profit]
    q =(len(month))
    q = q - 1
  
    #Iterate through the profit colums to find the differences between each months profit 
    get_profit = []
    for i in range(1,len(profit)):
        x = p[i] - p[i - 1]
        get_profit.append(x)
    
    #Sum the differences between the months, the cauculate the average
    v = (sum(get_profit))
    w = (v/q)
    w = round(w,2)
    
    #Print the average difference in profits 
    print(f"Average Change: $" + str(w) +"\n")
    
    #Identify maxmium value
    max_value = max(get_profit)
    max_index = (list.index(get_profit,max_value))
    max_index_month = max_index +1

    #Identify minmium value
    min_value = min(get_profit)
    min_index =(list.index(get_profit,min_value))
    min_index_month = min_index +1

    #Print out greatest increase and decrease
    print(f"Greatest Increase in Profits: "+ str(month[max_index_month]) + " ($" + str(get_profit[max_index]) + ")\n")
    print(f"Greatest Decrease in Profits: "+ str(month[min_index_month]) + " ($" + str(get_profit[min_index]) + ")\n\n")

    #Write to text file 
    output = os.path.join('analysis','Analysis.txt')
    with open(output,'w',newline= "\n") as text_file:
        text_file.write("Financial Analysis\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
        text_file.write(f"Total Months: " + str(len(month))+ "\n\n")
        text_file.write(f"Total $" + str(sum(p)) + "\n\n")
        text_file.write(f"Average Change: $" + str(w) +"\n\n")
        text_file.write(f"Greatest Increase in Profits: "+ str(month[max_index_month]) + " ($" + str(get_profit[max_index]) + ")\n\n")
        text_file.write(f"Greatest Decrease in Profits: "+ str(month[min_index_month]) + " ($" + str(get_profit[min_index]) + ")\n\n")


