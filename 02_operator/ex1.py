#연산자

#산술연산자
a=10
b=3

print(a+b) 
print(a-b) 
print(a*b) 
print(a/b) 
print(a//b)
print(a%b)
print(a**b)

a += 4
print(a)

#증감
a+=1

#비교연산
print(3==3.0)
print(3 != 4)
print("apple" < "apble")
print(1<2<3)
print(1<3<2)

#논리연산자
print(True and True)
print(True or False)
print(not True)

#short circuit
a = 10
b = 0

#print(a/b)

if a > 0 or a/b:
    print("yes")
else:
    print("no")

