class Solution:
    def firstMissingPositive(self, nums):

        n = len(nums)

        # Put every positive number x
        # at index x - 1
        for i in range(n):

            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:

                correct_index = nums[i] - 1

                nums[i], nums[correct_index] = (
                    nums[correct_index],
                    nums[i]
                )

        # Find the first incorrect position
        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        # All 1..n are present
        return n + 1
