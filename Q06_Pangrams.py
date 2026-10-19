# HackerRank: Pangrams
s = input().lower()
letters = set()

for char in s:
    if char.isalpha():
        letters.add(char)

print("pangram" if len(letters) == 26 else "not pangram")
