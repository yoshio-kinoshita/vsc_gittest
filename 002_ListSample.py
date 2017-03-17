squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])
print(squares[-1])
print(squares[-3:])

print(squares[:])

print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64

print(cubes)

cubes.append(216)
cubes.append(7 ** 3)

print(cubes)


for n in range(2,10):
    for x in range(2, ):
        if n % x == 0:
            print(n, 'equals')
