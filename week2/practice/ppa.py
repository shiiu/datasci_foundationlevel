string= str(input())

string= string.lower()

vowels= set()

for char in string:
    if char in 'aeiou':
        vowels.add(char)

sorted_vowels = sorted(vowels)

if sorted_vowels:
    print(' '.join(sorted_vowels))
else:
    print("none")

