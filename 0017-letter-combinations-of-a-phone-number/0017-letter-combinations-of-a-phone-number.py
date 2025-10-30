key={
    '1':'',
    '2':'abc',
    '3':'def',
    '4':'ghi',
    '5':'jkl',
    '6':'mno',
    '7':'pqrs',
    '8':'tuv',
    '9':'wxyz'
}
def key_word(s1):
    if s1 == '':
        return ['']
    
    ans=[]
    smallAns=s1[1:]
    smallrecurr=key_word(smallAns)

    keys=key[s1[0]]

    for mychar in keys:
        for char in smallrecurr:
            ans.append(mychar + char)
        
    return ans




class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        

        return key_word(digits)