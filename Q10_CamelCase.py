# HackerRank: CamelCase
s = input().strip()

if s:
    words = 1 + sum(1 for char in s if char.isupper())
    print(words)
else:
    print(0)
