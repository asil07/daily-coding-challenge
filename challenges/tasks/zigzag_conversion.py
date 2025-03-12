class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        index, step = 0, 1

        for char in s:
            rows[index] += char

            # Change direction when reaching the top or bottom row
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return "".join(rows)

# Example usage
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(sol.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(sol.convert("A", 1))               # Output: "A"
