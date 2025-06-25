class Solution(object):
    def isPathCrossing(self, path):
        x = y = 0
        vis = {(0, 0)}
        for c in path:
            if c == 'N':
                x -= 1
            if c == 'S':
                x += 1
            if c == 'E':
                y += 1
            if c == 'W':
                y -= 1
                
            if (x, y) in vis:
                return True
            vis.add((x, y))
        return False