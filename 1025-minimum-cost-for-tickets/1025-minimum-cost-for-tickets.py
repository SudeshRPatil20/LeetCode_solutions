class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        p = [0] * 366  
        travel_days = set(days)
        
        for i in range(1, 366):  
            if i not in travel_days:
                p[i] = p[i-1]
            else:
                p[i] = min(
                    p[i - 1] + costs[0],
                    p[max(0, i-7)] + costs[1],  
                    p[max(0, i-30)] + costs[2] 
                    )
        return p[365]
        