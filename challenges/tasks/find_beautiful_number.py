class Solution(object):
    def beautifulNumbers(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        def is_beautiful(n):
            digits = [int(d) for d in str(n)]
            digit_sum = sum(digits)
            digit_product = 1
            for d in digits:
                digit_product *= d
            
            return digit_sum != 0 and digit_product % digit_sum == 0
        
        count = 0
        for num in range(l, r + 1):
            if is_beautiful(num):
                count += 1
        
        return count
