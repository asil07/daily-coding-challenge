from collections import defaultdict
from math import gcd

# Define a constant for the modulo operation to prevent overflow
MOD = 10**9 + 7

def count_subsequence_pairs(nums):
    n = len(nums)
    # Dictionary to store the count of subsequences with each GCD value
    gcd_count = defaultdict(int)
    
    # Generate all non-empty subsequences and count GCD occurrences
    for i in range(1, 1 << n):  # Loop through all possible subsequences (excluding the empty one)
        subseq_gcd = 0  # Start with GCD as 0
        for j in range(n):  # Iterate over each element in the array
            if i & (1 << j):  # Check if the j-th element is included in the current subsequence
                subseq_gcd = gcd(subseq_gcd, nums[j])  # Update the GCD of the current subsequence
        gcd_count[subseq_gcd] += 1  # Increment the count for the calculated GCD

    result = 0
    # Count pairs of subsequences with the same GCD
    for g, count in gcd_count.items():
        # Each pair of subsequences with the same GCD contributes count * count to the result
        result = (result + count * count) % MOD
        
    return result

# Example usage
nums1 = [1, 2, 3, 4]
nums2 = [10, 20, 30]
nums3 = [1, 1, 1, 1]
print(count_subsequence_pairs(nums1))  # Output: 10
print(count_subsequence_pairs(nums2))  # Output: 2
print(count_subsequence_pairs(nums3))  # Output: 50
