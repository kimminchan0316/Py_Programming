for i in range(5):
    print(i,end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)

for i in range(1,6):
    print(i,end=" ")
print()

for i in range (1,11,2):
    print(i,end=" ")
print()

for i in range(10,0,-1):
    print(i,end=" ")
print()

s = 'Hello'

for c in s:
    print(c,end=" ")
print()

print(len(s))

#구구단
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}",end="\t")
    print()
else:
    print("End")
