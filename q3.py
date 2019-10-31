# Match last two digits to six digit lottery number
# Tracy Sun
from random import randint

#generate a six digit lottery number
num = randint(000000,999999)

#use modular to calculate the last two digits of the lottery number
last_two_digit = num%(10**2)
print(last_two_digit)

#first number should be 0000+last two digits
start = '0000'+str(last_two_digit)
list = []
list.append(start)
print(list)
print(start)
start = int(start)

#for every 100, keep adding to the last two digits to get the next value till 999999
while (start+100 <= 999999):
    next = start + 100
    start = next

    #add various number of 0's depending on how many digits we currently have
    #then append to the list
    if(len(str(start))==2):
        list.append('0000'+str(start))
    elif((len(str(start))==3)):
        list.append('000'+str(start))
    elif((len(str(start))==4)):
        list.append('00'+ str(start))
    elif((len(str(start))==5)):
        list.append('0'+ str(start))
    else:
        list.append(str(start))

print("The winning number is " + str(num))
print("Total number of result: ", len(list))
print("The output array should have:")
print(list)
