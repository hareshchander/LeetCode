class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        res = []

        while l < r:
            summ = numbers[l]+numbers[r]
            if summ < target:
                l+=1
            elif summ > target:
                r-=1
            else:
                res.append(l+1)
                res.append(r+1)
                return res