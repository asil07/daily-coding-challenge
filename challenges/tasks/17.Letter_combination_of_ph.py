class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to letters
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        # Backtracking helper function
        def backtrack(index, current_combination):
            # If the current combination is complete, add it to the result
            if index == len(digits):
                result.append("".join(current_combination))
                return

            # Get the letters corresponding to the current digit
            letters = digit_to_char[digits[index]]
            for letter in letters:
                # Add the letter to the current combination and move to the coming digit
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                # Backtrack by removing the last letter
                current_combination.pop()

        # Start the backtracking process
        backtrack(0, [])
        return result
