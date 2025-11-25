class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)

        vowel_indices = []
        vowel_chars = []

        for index, char in enumerate(s):
            if char in vowels:
                vowel_indices.append(index)
                vowel_chars.append(char)

        vowel_chars.reverse()

        for index, char in zip(vowel_indices, vowel_chars):
            s[index] = char

        return ''.join(s)
