# class Solution:
#     def missingNumber(self, nums):
#         if nums == [len(nums)-1]:
#             return 1
        
#         for i, v in enumerate(nums):
#             if i != v:
#                 print(i,v)
#                 return i
#             elif i in v:
#                 return i+1

class Solution:
    def missingNumber(self, nums):
        
        nums.sort()       
        i=enumerate(nums)
        b=len(nums)
        c = range(b)
        c = list(c)
        f=0
        while f <= len(nums):
            if nums[f] != c[f]:
                return c[f]
                
            elif nums == c:
                return (max(nums)+1)
                
            f += 1

s = Solution()
d = s.missingNumber([0,1,2,5,4])
print(d)