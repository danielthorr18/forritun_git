size = int(input("Input size: "))
arr = []
for i in range(size):
    arr.append(int(input('Enter value {}: '.format(i + 1))))

sum1 = 0

for i in arr:
    sum1 += i

average = sum1 / len(arr)
print('{} is the average!'.format(average))
