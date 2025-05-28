class Solution(object):
    def constructRectangle(self, area):
        w = 1
        while w * w <= area:
            w += 1
        w -= 1  
        while w > 0:
            if area % w == 0:
                return [area // w, w]
            w -= 1
        