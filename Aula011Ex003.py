matrix = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matrix[i].append(int(input(f"Matrix[{i}][{j}] =")))

print('='*10)
print(f"{f'MATRIX':^10}")
print('='*10)
for i in range(0, 3):
    for j in range(0, 3):
        print(f" {matrix[i][j]}", end=' ')
    print('')