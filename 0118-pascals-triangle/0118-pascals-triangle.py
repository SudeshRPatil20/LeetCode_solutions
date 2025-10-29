class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res =[[1]]
        for i in range(1, numRows):
            prev =res[-1]
            current = [1]
            for j in range(1, len(prev)):
                current.append(prev[j-1] + prev[j])
            current.append(1)
            res.append(current)
        return res




        # if numRows == 1:
        #     return [[1]]
        # b=[[1]]
        # for i in range(1, numRows):
        #     b.extend([[int(x) for x in str(11**i)]])
        # return b