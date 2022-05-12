#! usr/bin/env python3

"""
- input numbers para a lista
- ordenar lista
- print count, sum, lowest, highest, mean, median
"""

numbers = []
total = 0

def sort_list(unsorted_list):
    """sorting list """
    lenght = len(unsorted_list)
    swapped = True
    while swapped:
        swapped = False
        index = 0
        while index < lenght - 1:
            cur = unsorted_list[index]
            nxt = unsorted_list[index + 1]
            if cur > nxt:
                swapped = True
                unsorted_list[index] = nxt
                unsorted_list[index + 1] = cur
            index += 1
    return unsorted_list

while True:
    user_input = input('enter a number or Enter to finish: ')
    if not user_input:
        break
    try:
        number = int(user_input)
        total += number
        numbers.append(number)
    except ValueError as err:
        print(err)

if numbers:
    numbers = sort_list(numbers)
    COUNT = len(numbers)
    LOWEST = numbers[0]
    HIGHEST = numbers[-1]
    MEAN = total/COUNT

    HALF = len(numbers)//2
    median = numbers[HALF]
    if len(numbers)/2 == HALF:
        median = (median + numbers[HALF - 1])/2

    print('numbers: ', numbers)
    print('COUNT = ', COUNT, 'sum = ', total,
          'lowest = ', LOWEST, 'highest = ', HIGHEST,
          'mean = ', MEAN, 'median = ', median)