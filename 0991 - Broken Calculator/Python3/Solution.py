class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while startValue < target:
            if target % 2 == 0:
                target /= 2
            else:
                target += 1
        
            res += 1
        
        return int(res + startValue - target)