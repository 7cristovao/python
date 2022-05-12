#! usr/bin/env python3

numbers = []

while True:
    try:
        x = input("enter a number or Enter to finish: ")
        if not x:
            break
     except EOFError:
         break
#        numbers.append(int(line))
#    except ValueError as err:
#        print(err)

#count = len(numbers)
#total = sum(numbers)
#lowest = min(numbers)
#highest = max(numbers)
#mean = total / count

#print('numbers: ', numbers)
#print("count = {count} sum = {total} lowest = {lowest} highest = {highest} mean = {mean}".format( **locals() ) )
