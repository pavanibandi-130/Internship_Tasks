# Problem: Check Strict Superset
# HackerRank: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

a = set(map(int, input().split()))
n = int(input())

is_strict_superset = True

for _ in range(n):
    other = set(map(int, input().split()))
    if not (a > other):
        is_strict_superset = False

print(is_strict_superset)
