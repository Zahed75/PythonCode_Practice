#QUEE FIRST IN FIRST OUT
'''
Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
Front: Get the front item from queue – Time Complexity : O(1)
Rear: Get the last item from queue – Time Complexity : O(1)'''
from collections import deque

bank=deque(["Zahed","Hasan","Wakil","fahim","Shahrair"])
bank.popleft()#front theke data delete korbe
bank.popleft()#front theke data delete korbe
bank.popleft()#front theke data delete korbe
bank.popleft()#front theke data delete korbe
bank.popleft()#front theke data delete korbe

print(bank)
if not bank:
    print("No Person Left")
