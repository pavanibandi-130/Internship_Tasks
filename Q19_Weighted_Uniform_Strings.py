# HackerRank: Weighted Uniform Strings
s = input().strip()
n = int(input())
weights = set()
previous = ""
current_weight = 0

for char in s:
    value = ord(char) - ord('a') + 1

    if char == previous:
        current_weight += value
    else:
        current_weight = value
        previous = char

    weights.add(current_weight)

for _ in range(n):
    query = int(input())
    print("Yes" if query in weights else "No")
