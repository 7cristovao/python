l =[0,1,2,4,11]
#l[2] = l[2] % 2
#print(l)
#print(l[2])
i = 0
par = 0
impar = 0
for i in l:
	if i % 2 == 1:
	    print(i)
	    l.remove(i)
print(l)