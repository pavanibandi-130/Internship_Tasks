# HackerRank: Game of Thrones - I
from collections import Counter

s = input().strip()
frequencies = Counter(s)
odd_count = sum(1 for count in frequencies.values() if count % 2 != 0)

print("YES" if odd_count <= 1 else "NO")
