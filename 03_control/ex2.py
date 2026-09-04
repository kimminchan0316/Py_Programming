#반복문

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
i = 0
while i < len(nums):
    if nums[i] == target:
        print("찾")
        break
    i += 1

i = 1
tot = 0
while i <= 10:
    i += 1
    if i%2 == 1:
        continue
    tot += i
print(tot)

