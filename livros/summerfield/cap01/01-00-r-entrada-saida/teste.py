#! usr/bin/env python3

print("Type integers, wach followed by Enter; or just Enter to finish")

total = 0
count = 0

while True:
    line = input("integer: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += i
    else:
        break

if count:
    print("count =", count, "total =", total, "mean =", total / count)
