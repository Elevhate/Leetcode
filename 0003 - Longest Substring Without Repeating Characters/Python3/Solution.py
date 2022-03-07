class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = res = 0
        char = set()
        while right < len(s):
            if s[right] not in char:
                char.add(s[right])
                right += 1
            else:
                char.remove(s[left])
                res = max(res, right-left)
                left += 1
        res = max(res, right - left)
        return res