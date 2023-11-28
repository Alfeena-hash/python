import deque
list1=deque(["apple","orange","grapes"])
print(list1) #deque['apple','orange','grapes'])
list1.append("cherry")
print(list1) #deque(['apple','orange','grapes','cherry'])
list1.popleft()
print(list1) #deque(['orange','grapes','cherry'])

