from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.popleft()  # Output: 10
print("after popleft:", queue)  # Output: deque([20, 30])