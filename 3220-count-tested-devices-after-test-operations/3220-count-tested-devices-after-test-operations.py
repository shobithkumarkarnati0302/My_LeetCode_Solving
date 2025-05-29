class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        ans = 0
        for x in batteryPercentages:
            if x - ans > 0:
                ans += 1
        return ans
        