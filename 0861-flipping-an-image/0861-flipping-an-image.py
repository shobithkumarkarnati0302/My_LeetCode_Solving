class Solution(object):
    def flipAndInvertImage(self, image):
        row = len(image)
        for i in range(row):
            start =  0
            end = row-1
            while start <= end:
                image[i][start],image[i][end] = image[i][end]^1,image[i][start]^1
                start += 1
                end -= 1

        return image
        