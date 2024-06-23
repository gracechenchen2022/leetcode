class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i,j,n,ans,p=0,0,len(nums),0,1
        while j<n:
            f=True
            while i<n and p*nums[i]<k:
                p*=nums[i]
                i+=1
                f=False
            if i>j:
                if f:
                    if p<k:
                        ans+=(i-j)
                else:
                    ans+=(i-j)
                p=p//nums[j]
            j+=1
            if j>i:
                i=j
        return ans