# HackerRank: Super Reduced String
s = input().strip()
stack = []

for char in s:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)

result = "".join(stack)
print(result if result else "Empty String")
