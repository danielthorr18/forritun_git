def make_new_row(rows):
    if rows == 1: return [[1]]

    triangle = [[1], [1, 1]] 

    row = [1, 1] 

    for i in range(2, rows):
        row = [1] + [sum(column) for column in zip(row[1:], row)] + [1]
        triangle.append(row)

    return triangle

height = int(input("Height of Pascal's triangle (n>=1): "))
for row in make_new_row(height):
    print(row)