# Problem: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

n = int(input())
heights = set(map(int, input().split()))

print(sum(heights) / len(heights))
