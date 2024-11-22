from collections import deque

def stack():
 num_input = input()
 nums = list(map(int, num_input.split()))

 num_stack = deque()

 for num in nums:
    num_stack.append(num)

 print(num_stack)

 while num_stack:
    num = num_stack.pop()
    print(num * 2)

stack()