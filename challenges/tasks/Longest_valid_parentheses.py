class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize stack with -1 to handle edge cases
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push index of '('
            else:
                stack.pop()  # Pop last '(' index
                if not stack:
                    stack.append(i)  # Push current ')' index to handle next valid substrings
                else:
                    max_length = max(max_length, i - stack[-1])  # Compute length
        
        return max_length
