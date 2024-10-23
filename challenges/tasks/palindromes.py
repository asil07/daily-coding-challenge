class Solution(object):
    def findAnswer(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[bool]
        """
        from collections import defaultdict
        
        n = len(parent)
        
        # Build the tree using the parent array
        tree = defaultdict(list)
        for i in range(1, n):
            tree[parent[i]].append(i)
        
        # Function to check if a given string is a palindrome
        def is_palindrome(st):
            return st == st[::-1]
        
        # DFS function to collect characters
        def dfs(x):
            dfsStr = []
            
            # Inner recursive DFS function
            def dfs_inner(node):
                for child in sorted(tree[node]):
                    dfs_inner(child)
                dfsStr.append(s[node])
            
            # Start DFS from the current node x
            dfs_inner(x)
            # Return True if the collected string is a palindrome
            return is_palindrome(''.join(dfsStr))
        
        # Result array
        answer = [False] * n
        
        # Perform the DFS for each node and check the palindrome condition
        for i in range(n):
            answer[i] = dfs(i)
        
        return answer
