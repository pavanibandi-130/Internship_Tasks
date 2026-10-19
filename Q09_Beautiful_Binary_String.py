# HackerRank: Beautiful Binary String
n = int(input())
b = input().strip()
count = 0
i = 0

while i <= len(b) - 3:
    if b[i:i + 3] == "010":
        count += 1
        i += 3
    else:
        i += 1

print(count)
