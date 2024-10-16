class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for num in nums:
            found = False
            # Loop through possible values of ans[i] from 0 to num
            for i in range(num):
                if (i | (i + 1)) == num:
                    ans.append(i)
                    found = True
                    break
            # If no value is found that satisfies the condition, append -1
            if not found:
                ans.append(-1)

        return ans

# Example usage
sol = Solution()
nums1 = [2, 3, 5, 7]
nums2 = [11, 13, 31]
print(sol.minBitwiseArray(nums1))  # Output: [-1, 1, 4, 3]
print(sol.minBitwiseArray(nums2))  # Output: [9, 12, 15]