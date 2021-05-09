vowels = ['a','e','i','o','u']
word = input("Podaj slowo, ktory nalezy wyszukac samogloski: ")
found = []
for letter in word:
    if letter in vowels:
        found.append(letter)

for vowel in found:
    print(vowel)