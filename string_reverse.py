from stack import Stack

monte = Stack()

s = input()

for l in s:
    monte.push(l)
    
r = "".join([monte.pop() for _ in s])

print(r)