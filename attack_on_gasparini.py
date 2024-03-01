from time import time

# n, x = map(int, input().split())
# titan_sizes = input()
# P, M, G = map(int, input().split())

n, x = 30000, 1000
titan_sizes = 'PMG' * 10000
P, M, G = 1000, 1000, 1000

titan_values = {
    "P": P,
    "M": M,
    "G": G
}

wall_heights = [x]
num_walls = 1

start = time()

for i, titan_size in enumerate(titan_sizes):
    titan_value = titan_values[titan_size]
    for j in range(num_walls):
        wall = wall_heights[j]
        if wall >= titan_value:
            wall_heights[j] -= titan_value
            break
        else:
            if j == num_walls - 1:
                wall_heights.append(x - titan_value)
                num_walls += 1
    
print(num_walls)

print("Time:", time() - start)
        

