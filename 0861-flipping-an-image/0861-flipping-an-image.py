class Solution(object):
    def flipAndInvertImage(self, image):
        row = len(image)
        col = len(image[0])

        for i in range(row):
            start =  0
            end = col-1

            while start <= end:
                image[i][start],image[i][end] = image[i][end]^1,image[i][start]^1
                start += 1
                end -= 1
            
        # for i in range(row):
        #     for j in range(col):
        #         if image[i][j] == 0:
        #             image[i][j] = 1
        #         else:
        #             image[i][j] = 0

        return image
        