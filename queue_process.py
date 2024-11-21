from collections import deque

input = input()
words = input.split()

queue = deque(words)
print(queue)

while queue:
    word = queue.popleft()  
    if 'a' in word.lower():  
        print(word)