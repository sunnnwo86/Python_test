# class Solution:
#     def findDuplicate(self, nums):

nums =[1,2,3,4,3]
a = nums.count(3)        
print(a)


b = 1
while b <= len(nums):

    if nums.count(b) != 1:
        print("중복이네", b)
        break 
    b+=1