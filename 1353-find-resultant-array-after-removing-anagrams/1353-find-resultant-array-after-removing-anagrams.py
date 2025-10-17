class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        arr = {}
        array = []

        prevev_element=""



        for ele in words:
            s="".join(sorted(ele))

            if s != prevev_element:
                array.append(ele)
            
            prevev_element = s
            



            # if s not in arr and ele not in array:
            #     array.append(ele)
            #     arr[s]= [ele]
            # else:
                
            #     arr[s].append(ele)
        return array