class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        print(f'lens of ratings {n}')
        candies = [1] * n
        print(f'Candies at first: {candies}')
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                print(f"candies[i] = candies[i - 1] + 1:::: {candies}")
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
                print(f'Chapdan onga hisoblagandagi holat:{candies}')
        return sum(candies)
           

candy = Solution().candy     
ratings1 = [1, 0, 2]
ratings2 = [1, 2, 2]

print(candy(ratings1))  # Natija: 5
print(candy(ratings2))  # Natija: 4
               