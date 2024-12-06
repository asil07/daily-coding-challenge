class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Initialize three pointers
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:  # If the color is red (0)
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # If the color is white (1)
                mid += 1
            else:  # If the color is blue (2)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        return nums  # This step is optional as the sorting is done in-place
