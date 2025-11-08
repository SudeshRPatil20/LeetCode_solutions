class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d={}

        # translator = str.maketrans('', '', string.punctuation)

        for char in re.sub(r'[^a-zA-Z0-9\s]', ' ', paragraph).lower().split():
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

            if char in banned:
                d.pop(char)
        return max(d, key=d.get)
