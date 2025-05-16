class Solution(object):
    def oddCells(self, m, n, indices):

        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]

        for row,col in indices:
            rows[row] += 1
            cols[col] += 1
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if (rows[i]+cols[j])%2 == 1:
                    res += 1 
        
        return res

