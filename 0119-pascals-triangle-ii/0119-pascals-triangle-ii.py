class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        res =[[1]]
        for i in range(1, rowIndex+1):
            prev =res[-1]
            current = [1]
            for j in range(1, len(prev)):
                current.append(prev[j-1] + prev[j])
            current.append(1)
            res.append(current)
        return res[rowIndex]
        