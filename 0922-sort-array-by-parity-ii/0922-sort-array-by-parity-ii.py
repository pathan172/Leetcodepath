class Solution:
    def sortArrayByParityII(self, nums):
        ans = [0] * len(nums)

        even = 0
        odd = 1

        for x in nums:
            if x % 2 == 0:
                ans[even] = x
                even += 2
            else:
                ans[odd] = x
                odd += 2

        return ans