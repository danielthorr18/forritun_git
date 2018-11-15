size = int(input("Input size: "))
arr = []
for i in range(size):
    arr.append(int(input('Enter value {}: '.format(i + 1))))

unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print('{} is the original!'.format(arr))

print('{} er hins vegar unique!'.format(unique))