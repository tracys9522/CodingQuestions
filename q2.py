# Read csv file and sort people's last name
# Tracy Sun

import csv

#open the csv file
data = csv.reader(open('q2.csv'))

#take out the header
header = data.next()

#sort function to sort by last name
sort_data = sorted(data, key = lambda row:row[1])

#print statement
for row in sort_data:
    print(row[0]+row[1])
