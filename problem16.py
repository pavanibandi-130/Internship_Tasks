# Problem: Check Subset
# HackerRank: https://www.hackerrank.com/challenges/py-check-subset/problem

t = int(input())

for _ in range(t):
    n_a = int(input())
    a = set(map(int, input().split()))

    n_b = int(input())
    b = set(map(int, input().split()))

    print(a.issubset(b))
