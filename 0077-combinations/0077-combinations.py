from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        res = []

        for c in combinations(range(1, n + 1), k):
            res.append(list(c))

        return res


