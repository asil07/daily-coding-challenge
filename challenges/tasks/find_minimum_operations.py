class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = 0
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                counts += 1
            elif remainder == 2:
                counts += 1
        return counts


countr = Solution()

print(f"result: {countr.minimumOperations([1, 2, 3, 4])}")