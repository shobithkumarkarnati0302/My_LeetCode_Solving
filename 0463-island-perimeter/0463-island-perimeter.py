class Solution(object):
    def islandPerimeter(self, grid):
        peri = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:

                    #checking up side
                    if row == 0 or grid[row - 1][col] == 0:
                        peri += 1

                    #checking down side
                    if row == len(grid) - 1 or grid[row + 1][col] == 0:
                        peri += 1

                    #checking left side
                    if col == 0 or grid[row][col-1] == 0:
                        peri += 1

                    #checking right side
                    if col == len(grid[0]) - 1 or grid[row][col+1] == 0:
                        peri += 1

        return peri
