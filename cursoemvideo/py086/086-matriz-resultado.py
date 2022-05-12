x =[[[],[],[]],[[],[],[]],[[],[],[]]]
i = 0
v = list()
for i in range(0,9):
	v.append(int(input('')))
print('fim')
#print(v)
x[0][0] = v[0]
x[0][1] = v[1]
x[0][2] = v[2]
x[1][0] = v[3]
x[1][1] = v[4]
x[1][2] = v[5]
x[2][0] = v[6]
x[2][1] = v[7]
x[2][2] = v[8]
print(x)