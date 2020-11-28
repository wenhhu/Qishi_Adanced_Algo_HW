# LC 338

class Problem1:
    def countBits(self, num: int) -> List[int]:
        res, cur = [0]*(num+1), 1
        for i in range(1, num+1):
            if cur*2 <= i:
                cur *= 2
            res[i] = res[i-cur]+1
        return res

# LC 477

class Problem2:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in zip(*map('{:032b}'.format, nums)):
            res += (len(nums)-i.count('0'))*i.count('0')
        return res