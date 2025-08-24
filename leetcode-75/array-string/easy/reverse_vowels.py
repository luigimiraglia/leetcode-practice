# Problem: Reverse Vowels of a String
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Difficulty: Easy
# Approach: Identify vowels, store them in order, then rebuild the string replacing vowels in reverse order.

def reverseVowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    letters = list(s)
    only_vowels = [char for char in letters if char in vowels]

    i = len(only_vowels)
    result = []

    for char in letters:
        if char in vowels:
            i -= 1
            result.append(only_vowels[i])
        else:
            result.append(char)

    return "".join(result)
