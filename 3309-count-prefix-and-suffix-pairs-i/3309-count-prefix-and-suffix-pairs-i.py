class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        word_combination = combinations(words, 2)
        count = 0

        for i in word_combination:
            if i[1].startswith(i[0]) and i[1].endswith(i[0]):
                count += 1
            
        return count