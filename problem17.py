# Problem 17: Finding the Percentage
# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
students = {}

for _ in range(n):
    data = input().split()
    students[data[0]] = list(map(float, data[1:]))

name = input()
marks = students[name]
print(f"{sum(marks) / len(marks):.2f}")
