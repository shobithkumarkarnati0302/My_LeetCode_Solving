class Solution(object):
    #helper function
    def binary(self,arr,start,end,target):
        if start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] <= target:
                return self.binary(arr, mid + 1, end, target)
            else:
                return self.binary(arr, start, mid - 1, target)
        return -1

    def search(self, arr, target):
        start = 0
        end = len(arr)-1
        return self.binary(arr,start,end,target)
        