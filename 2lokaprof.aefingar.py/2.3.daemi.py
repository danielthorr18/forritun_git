size = int(input("Input size: "))
arr = []
for i in range(size):
    arr.append(int(input('Enter value {}: '.format(i + 1))))

target = int(input('Input target: '))

found = 0
for i in arr:
    if target == i:
        found += 1

print('{} is {} times in the list.'.format(target, found))