h, z, l = input().split()

middle = sorted([h, z, l])[1]

if h == middle:  
    print('huguinho')
elif l == middle:
    print('luisinho')
else:
    print('zezinho')