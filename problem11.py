# Problem: Text Wrap
# HackerRank: https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

text = input()
width = int(input())

print(textwrap.fill(text, width))
