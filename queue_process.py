from collections import deque

def queue_stack():
    word_input = input()
    words = word_input.split()

    queue = deque(words)
    print(queue)

    for word in queue:
        if 'a' in word.lower():
            print(word)

queue_stack()
