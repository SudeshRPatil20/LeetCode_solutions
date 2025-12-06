class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cache = {}    
        count = 0

        def is_subseq(w):
            i = j = 0
            while i < len(s) and j < len(w):
                if s[i] == w[j]:
                    j += 1
                i += 1
            return j == len(w)

        for w in words:
            if w in cache:
                count += cache[w]
            else:
                res = 1 if is_subseq(w) else 0
                cache[w] = res
                count += res

        return count





        # if len(words) < 1:
        #     return 0
        # char = words[0]
        # i = 0
        # j = 0
        # while j < len(char) and i < len(s):
        #     if s[i] == char[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         i += 1

        # if  j == len(char):
        #     count = 1
        # else:
        #     count = 0
        # return count + self.numMatchingSubseq(s, words[1:])
        
