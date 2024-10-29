def length_after_transformations(s, t):
    mod = 10**9 + 7
    count_z = s.count('z')
    length = len(s)
    
    for _ in range(t):
        length = (length + count_z) % mod
        count_z = (2 * count_z) % mod
    
    return length

# Example usage
s1 = "abcyy"
t1 = 2
print(length_after_transformations(s1, t1))  # Output: 7

s2 = "azbk"
t2 = 1
print(length_after_transformations(s2, t2))  # Output: 5
