class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        # Minimum possible maximum gap
        gap = max(1, (max_val - min_val + n - 2) // (n - 1))

        bucket_count = (max_val - min_val) // gap + 1

        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count

        # Put values into buckets
        for num in nums:
            index = (num - min_val) // gap

            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)

        answer = 0
        previous_max = min_val

        # Compare consecutive non-empty buckets
        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):
                continue

            answer = max(answer, bucket_min[i] - previous_max)
            previous_max = bucket_max[i]

        return answer
