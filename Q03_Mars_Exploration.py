# HackerRank: Mars Exploration
s = input().strip()
expected = "SOS"
changed = 0

for i, char in enumerate(s):
    if char != expected[i % 3]:
        changed += 1

print(changed)
