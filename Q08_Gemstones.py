# HackerRank: Gemstones
n = int(input())
common = set(input().strip())

for _ in range(n - 1):
    rocks = set(input().strip())
    common = common.intersection(rocks)

print(len(common))
