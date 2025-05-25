class Solution(object):
    def largestInteger(self, num):
        s = str(num)
        even_digits = sorted([int(d) for d in s if int(d) % 2 == 0], reverse=True)
        odd_digits = sorted([int(d) for d in s if int(d) % 2 != 0], reverse=True)

        even_index = 0
        odd_index = 0
        result = []

        for digit in s:
            if int(digit) % 2 == 0:
                result.append(str(even_digits[even_index]))
                even_index += 1
            else:
                result.append(str(odd_digits[odd_index]))
                odd_index += 1

        return int("".join(result))