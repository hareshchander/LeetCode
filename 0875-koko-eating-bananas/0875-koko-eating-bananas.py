class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

#We use binary search because the required hours decrease monotonically as eating speed increases, letting us efficiently find the minimum feasible speed.

        l, r = 1, max(piles)
        ans = r

        while l <= r:
            mid = (l+r)//2

#Cieling is used here to make sure we correctly count every partial hour as a full hour.
            hour = 0
            for p in piles:
                hour += (p + mid - 1)//mid

            if hour <= h:
                ans = mid
                r = mid - 1

            else:
                l = mid + 1
        return ans
