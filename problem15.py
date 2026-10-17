# Problem: Lists
# HackerRank: https://www.hackerrank.com/challenges/python-lists/problem

items = []

for _ in range(int(input())):
    command = input().split()
    action = command[0]

    if action == "insert":
        items.insert(int(command[1]), int(command[2]))
    elif action == "print":
        print(items)
    elif action == "remove":
        items.remove(int(command[1]))
    elif action == "append":
        items.append(int(command[1]))
    elif action == "sort":
        items.sort()
    elif action == "pop":
        items.pop()
    elif action == "reverse":
        items.reverse()
