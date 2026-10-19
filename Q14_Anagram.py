# HackerRank: Anagram
from collections import Counter

q = int(input())
for _ in range(q):
    s = input().strip()
    n = len(s)

    if n % 2 != 0:
        print(-1)
    else:
        first = Counter(s[:n // 2])
        second = Counter(s[n // 2:])
        changes = sum((first - second).values())
        print(changes)
