class Solution:
    def plusOne(self, digits):
           
        a = digits

        b = 10 **(len(a)-1) 

        
        c = 1
        d = 0
        while c <= len(a):

            for aa in a:

                b = 10 **(len(a)-(c))
                d += aa * b

                c += 1
        print(d)
        d += 1
        
        dd = str(d)

        dd = list(dd)
        print(dd)
        f = 0
        while f <= len(dd)-1:
            for ddd in dd:
                dd[f] = int(ddd)
                f += 1
        return dd


s = Solution()
p = s.plusOne([2,0,4])
print(p)






#         for b in digits[-1:]:
#             if digits[-1] == 9:
#                 digits.insert(-1,1)
#                 digits.insert(-1,0)
#                 digits.pop(-1)        
#             else:
#                 digits.insert(-1,b+1)
#                 digits.pop(-1)
            
#         return digits


# s = Solution()
# p = s.plusOne([2,3,4,5,9])
# print(p)

# a = str(123)
# a = list(a)
# print(a)
# a = tuple(a)
# print(a)
# a = list(a)
# a[0] = int(a[0])+1
# print(a)


# a = [1,2,9]

# b = 10 **(len(a)-1) 

# print(b)
# c = 1
# d = 0
# while c <= len(a):

#     for aa in a:

#         b = 10 **(len(a)-(c))
#         d += aa * b

#         c += 1
# d += 1
# print("d:",d)
# dd = str(d)

# dd = list(dd)
# print(dd)
# f = 0
# while f <= len(dd)-1:
#     for ddd in dd:
#         dd[f] = int(ddd)
#         f += 1
# print(dd)
#asdasdasd
