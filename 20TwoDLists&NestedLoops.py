number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
] #creates a grid like structure

print(number_grid[0][2])

for row in number_grid:
    for column in row:
        print(column)