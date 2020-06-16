class Solution:
    def countPrimes(self, n):



        
        
        a=range(n)

        a = list(a)
        c=[]

        if n ==0:
            return 0
        if n > 2:
            c =[2]
        if n > 3:
            c =[2,3]
        if n > 5:
            c =[2,3,5]
        if n > 7:
            c =[2,3,5,7]        
        for i in a:        
        
            if i%2 != 0: 

                c.append(i)
            for i in a:        
        
                if i%3 != 0:

                    c.append(i)
                    for i in a:        
        
                        if i%5 != 0:

                            c.append(i)
                            for i in a:        
        
                                if i%7 !=0:

                                    c.append(i)                
        if 1 in c:
            c.remove(1)
        return len(c)
s = Solution()
p = s.countPrimes(10)
print(p)


# # c.remove(1)        
# print(c)
# # print(len(c))
# class Solution:
#     def countPrimes(self, n: int) -> int:
        
        
        # a=range(n+1)

        # a = list(a)
        # c=[]
        # if n == 0:
        #     return 0
        # if n > 2:
        #     c =[2]
        # if n > 3:
        #     c =[2,3]
        # if n > 5:
        #     c =[2,3,5]
        # if n > 7:
        #     c =[2,3,5,7]        
        # for i in a:        
        
        #     if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 !=0:
                
        #         c.append(i)
        #         if 1 in c:
        #             c.remove(1)
                    
#         #     return c
# s = Solution()
# p = s.countPrimes(10000)
# print(p)