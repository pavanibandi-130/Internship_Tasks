# HackerRank: Separate the Numbers
q = int(input())
for _ in range(q):
    s = input().strip()
    found = False

    for length in range(1, len(s) // 2 + 1):
        first = s[:length]
        number = int(first)
        current = first

        while len(current) < len(s):
            number += 1
            current += str(number)

        if current == s:
            print("YES", first)
            found = True
            break

    if not found:
        print("NO")
