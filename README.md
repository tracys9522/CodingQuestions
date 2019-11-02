# CodingQuestions
Tracy Sun
Backend Developer Questions - Junior & Mid Level

Instructions:
After unzip the file, open your terminal and 'cd' into unzipped file directory

With all the python source code files, run it with python 'filename'.py

 q1 - q1.py
 Run: python q1.py
 Description: This file execute the two given example to calculate total profit.
 Output: 14796 and 32411

 q2 - q2.py & q2.csv
 Run: python q2.py
 Description: This file reads csv file and output info.
 Output: 
 Frodo Baggins
 Bill Gates
 Steve Jobs
 Michael Jordan
 Barack Obama
 Christian Ronaldo
 Michael Schumacher
 Tiger Woods

 q3 - q3.py
 Run: python p3.py
 Description: This file outputs all possible combinations that match the last two digit of a randomly generated 6 digit number.
 Output: 
 The winning number is 431117
 ('Total number of result: ', 10000)
 The output array should have:
 ['000017', '000117', '000217', '000317'...]

 q4 - q4.py
 Run: python p4.py
 Description: This file generates all permutations for a six digit number.
 Output: 
 The winning number is 909148
 The output array should have:
 [909184, 909841, 908149, 989140, 809149, 909418, 904198, 949108, 409198, 901948, 919048, 109948, 990148, 99148]

 q5 - q5.py & init.db
 Run: python q5.py
 Description: This file generates init.db which contains a SQLite table car with info and outputs the db results.
 Note that if you already have a SQLite table called 'car', un-comment in q5.py line 6 to drop your table first.
 Output:
 Rick, Corvette Z06
 Rick, Lotus Exite S
 Rick, BMW M3
 John, BMW 320d
 John, Mercedes SLK AMG
 Zing, Toyota Alphard
 Zing, Mercedes Sprinter
 Nan, Toyota Camry
 Nan, Porsche 911
 Nan, BMW M5
 Nan, Jaguar
 Nan, TukTuk
 Nan, Mini Cooper
 Nan, Honda Jazz

 q6 - q6.py
 Run: python q6.py
 Description: This file uses existing car table to output total count for each person.
 Note that you need to have SQLite table car. If not, please run q5.py to generate the table first.
 Output:
 John, 2
 Nan, 7
 Rick, 3
 Zing, 2

 q7 - q7.py
 Run: python q7.py
 Description: This file uses car table to output people who have more than 2 cars.
 Note that you need to make sure you have the car table created. If not, please run q5 first.
 Output:
 Nan, 7
 Rick, 3
