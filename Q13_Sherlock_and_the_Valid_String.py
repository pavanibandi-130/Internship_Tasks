# HackerRank: Sherlock and the Valid String
from collections import Counter

s = input().strip()
frequencies = Counter(Counter(s).values())

if len(frequencies) == 1:
    print("YES")
elif len(frequencies) == 2:
    items = sorted(frequencies.items())
    (f1, c1), (f2, c2) = items

    if (f1 == 1 and c1 == 1) or (f2 == f1 + 1 and c2 == 1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
