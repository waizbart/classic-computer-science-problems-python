a, b, c = map(int, input().split())

diff_ab = b - a
diff_bc = c - b

if diff_ab < 0:
    if diff_bc > diff_ab:
        print(':)')
    else:
        print(':(')
elif diff_ab > 0:
    if diff_bc < diff_ab:
        print(':(')
    else:
        print(':)')
else:
    if diff_bc > diff_ab:
        print(':)')
    else:
        print(':(')

