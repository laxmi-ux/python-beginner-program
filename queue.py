from collections import deque

# initiaize he empty queue
queue=deque()

#enque the element in the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

front=queue[0]
print("front element", front)

head=queue[-1]
print("front element", head)
 
#deque the element
deque_1= queue.popleft()
print("deque element", deque_1)
deque_2= queue.popleft()
print("deque second element",deque_2)

if not queue:
    print("queue is empty")
else:
    print("queue is not empty")    

print("Current queue",queue)