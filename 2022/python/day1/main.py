
with open("input.txt", "r") as inp:
    data = inp.readlines()

biggest_sum = [0]
temp = 0
for row in data:
    if row == "\n":
        if temp > biggest_sum[-1]:
            biggest_sum.append(temp)
            biggest_sum.sort(reverse=True)
            biggest_sum = biggest_sum[:3]
        temp = 0
    else:
        temp += int(row)

print(f"The answer to first part is {biggest_sum[0]}")
print(f"The top 3 are {biggest_sum}")
print(f"The total of the 3 is {sum(biggest_sum)}")

