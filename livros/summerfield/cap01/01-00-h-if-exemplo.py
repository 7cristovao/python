#! usr/bin/env python3

x = True
lines = 0
if x:
    print("x is nonzero")

if lines < 1000:
    print("small")
elif lines < 10000:
    print("medium")
else:
    print("large")
