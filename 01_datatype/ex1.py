#변수
#동적 타이핑 언어
a=2
b=3
#print(a, b)
print(a, end=" ")
print(b)
print(a, b, sep=",")
a=(2,b)
print(a)
print(type(a))

a=2; b=2
print(a,b)
x=y=z=0

a, b = (2, 3), 3
print(type(a), type(b))

a,b=2,3 # 튜플 언패킹
print(type(a), type(b))


#값 swap
tmp = a
a = b
b = tmp
print(a, b)

a, b = b, a
print(a, b)

#변수명 규칙(C랑 동일)
#문자, 숫자, 언더바만 가능
#숫자로 시작 불가
#대소문자 구문
#예약어 사용 불가
name2 = "pororo"
# 2name = "pororo"
_name = "pororo"
# class = "test"
# name! = "test"
이름 = "뽀로로"
print(이름)

snake_case = "뽀로로"
camelCase = "뽀로로"
MAX_VALUE = 100


