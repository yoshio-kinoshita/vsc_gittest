# リストサンプル
fruites = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruites.count('apple'))

print(fruites.count('tangerine'))

print(fruites.index('banana'))

print(fruites.index('banana', 4))

fruites.reverse()
print(fruites)

fruites.sort()
print(fruites)

print(fruites.pop())

# リストをスタックとして使う
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

# リストをキューとして使う

