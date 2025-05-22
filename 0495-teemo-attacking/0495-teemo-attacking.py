class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        def pairwise(iterable):
            it = iter(iterable)
            prev = next(it, None)
            for item in it:
                yield prev, item
                prev = item

        if not timeSeries:
            return 0

        ans = 0
        for a, b in pairwise(timeSeries):
            ans += min(duration, b - a)
        ans += duration
        return ans
