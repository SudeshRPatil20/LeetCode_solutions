class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_in_mag = {}
        char_in_ransomNote = {}

        for char in magazine:
            if char in char_in_mag:
                char_in_mag[char] += 1
            else:
                char_in_mag[char] = 1

        for char in ransomNote:
            if char in char_in_ransomNote:
                char_in_ransomNote[char] += 1
            else:
                char_in_ransomNote[char] = 1

        for char in ransomNote:
            if char not in char_in_mag or char_in_mag[char] < char_in_ransomNote[char]:
                return False

        return True
