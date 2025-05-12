class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=set(nums)
        nums.clear()
        for i in k:
            nums.append(i)
        nums.sort()
        return len(nums)
