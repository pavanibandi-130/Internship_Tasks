# Problem: Merge the Tools!
# HackerRank: https://www.hackerrank.com/challenges/merge-the-tools/problem

string = input().strip()
k = int(input())

for start in range(0, len(string), k):
    segment = string[start:start + k]
    seen = set()
    result = []

    for char in segment:
        if char not in seen:
            result.append(char)
            seen.add(char)

    print("".join(result))
