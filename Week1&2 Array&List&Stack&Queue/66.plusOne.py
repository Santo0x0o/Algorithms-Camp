https://leetcode-cn.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        while n >= 0:
            if digits[n] == 9:
                digits[n] = (digits[n] + 1) % 10
                if n == 0:
                    return [1] + digits
            else:
                digits[n] += 1
                return digits
            n -= 1


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        while n > 0:
            if digits[n] == 9:
                digits[n] = (digits[n] + 1) % 10
            else:
                digits[n] += 1
                return digits
            n -= 1
        if digits[0] == 9:
            digits[0] = (digits[n] + 1) % 10
            return [1] + digits
        else:
            digits[0] += 1
            return digits
