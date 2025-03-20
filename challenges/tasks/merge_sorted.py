class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
                # Start merging from the end of nums1
        p1, p2, p = m - 1, n - 1, m + n - 1  

        # While there are elements in nums2
        while p2 >= 0:
            
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        return p
        
funk = Solution()

amal = funk.merge(nums1 = [1,2,3,0,0,0], m=2, nums2 = [2,5,6], n=3)
print(amal)