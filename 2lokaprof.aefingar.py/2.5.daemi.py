size = int(input("Input size: "))
arr = []
for i in range(size):
    arr.append(int(input('Enter value {}: '.format(i + 1))))

lowest = float('inf')


if size > 0:
    lowest = arr[0]


    for i in range(1, len(arr)):
        if arr[i] < lowest:
            lowest = arr[i]

    print('{} is the lowest!'.format(lowest))

else:
    print('það er enginn listi fíflið þitt!')