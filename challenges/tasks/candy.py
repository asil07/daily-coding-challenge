import heapq

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
    


    def candy_heapq(ratings):
        n = len(ratings)
        candies = [1] * n  # Har bir bolaga kamida 1 ta shirinlik beramiz
        heap = []
        
        # Prioritet navbatga (min heap) barcha bolalarni qo'shamiz
        for i in range(n):
            heapq.heappush(heap, (ratings[i], i))
        
        # Prioritet navbatdan eng past reytingli bolalardan boshlaymiz
        while heap:
            rating, i = heapq.heappop(heap)
            
            # Chapdagi qo'shni bilan taqqoslaymiz
            if i > 0 and ratings[i] > ratings[i - 1]:
                candies[i] = max(candies[i], candies[i - 1] + 1)
            
            # O'ngdagi qo'shni bilan taqqoslaymiz
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Umumiy shirinliklar sonini qaytaramiz
        return sum(candies)

candy = Solution().candy     
ratings1 = [1, 0, 2]
ratings2 = [1, 2, 2]

print(candy(ratings1))  # Natija: 5
print(candy(ratings2))  # Natija: 4
               