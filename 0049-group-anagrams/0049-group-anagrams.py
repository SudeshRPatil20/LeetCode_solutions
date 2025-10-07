class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map={}

        for word in strs:
            key="".join(sorted(word))

            if key in anagrams_map:
                anagrams_map[key].append(word)
            else:
                anagrams_map[key]=[word]
            
        return [group for group in anagrams_map.values()]