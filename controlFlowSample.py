# if 文

# x = int(input("Please enter an integer:"))

# if x < 0:
#     x = 0
#     print('Nagetive changed to Zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# for 文
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


for w in words[:]:
    if(len(w) > 6):
        words.insert(0, w)

print(words)


for i in range(5):
    print(i)
for i in range(5, 10):
    print(i)
for i in range(0, 10, 3):
    print(i)
for i in range(-10, -100, -30):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


print(range(10))
print(list(range(10)))

print(list(range(2, 2)))
print(list(range(3, 4)))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')