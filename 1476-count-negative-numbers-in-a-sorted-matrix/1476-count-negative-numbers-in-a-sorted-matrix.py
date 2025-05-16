class Solution(object):
    def countNegatives(self, grid):
        l = len(grid)
        res = 0
        for x in grid:
            for y in x:
                if y<0:
                    res += 1
        return res