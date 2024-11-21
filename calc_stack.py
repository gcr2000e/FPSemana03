from collections import deque

input = input()
num = list(map(int, input.split()))

stack = deque(num)
print(stack)

while stack:
    num = stack.pop()
    print(num * 2)