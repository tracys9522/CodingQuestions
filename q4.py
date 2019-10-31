# All possible mutation for the input number
# Tracy Sun

from random import randint
import copy

#generate a six digit lottery number
num = randint(000000,999999)
num_str = str(num)
list = []

'''
#extreme test cases
num = 555555
num_str = str(num)
list = []
'''

input = []
#insert each digit into the list for swapping later
for i in range(len(num_str)):
    input.append(num_str[i])
print(input)
#algorithm to swap the digits
i = len(input)-1 #it for the last element

while(i >= 0):
    j = i - 1

    while(j>=0):
        #hard copy input
        temp = copy.copy(input)

        if(int(temp[i]) != int(temp[j])):
            #swap values at position i and position j
            temp_num = temp[i]
            temp[i] = temp[j]
            temp[j] = temp_num

            #append result into list
            list.append(temp)
        j-=1
    i -= 1
print("The winning number is " + str(num))
print("The output array should have:")
result = []

if(len(list) == 0):
    result = num

#print out nicely looking results
for item in list:
    array = ""
    for letter in item:
        array+=str(letter)
    result.append(int(array))
print(result)
