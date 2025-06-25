class Solution(object):
    def helper(self, x):
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(x[:2])
        day = int(x[3:])
        return sum(days_per_month[:month - 1]) + day


    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if start > end:
            return 0

        diff = self.helper(end) - self.helper(start)
        return diff + 1
        