class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        k=len(nums)
        j=1
        for i in range(k):
            while (nums[i]-i)%2!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
            j=i+1
        return nums