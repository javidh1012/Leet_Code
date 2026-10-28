class Solution:
    def isHappy(self, n: int) -> bool:
    #     visited = set()

    #     while n not in visited:
    #         visited.add(n)
    #         n = self.sumofsquare(n)

    #         if n == 1:
    #             return True
    #     return False

    # def sumofsquare(self, n: int) -> int:
    #     op = 0
    #     while n :
    #         digit = (n % 10)**2
    #         op +=digit
    #         n = n //10
    #     return op




        if n==1 or n==7:
            return True
        elif n<10:
            return False
        else:
            sum = 0
            while n > 0:
                temp = n%10
                sum += temp * temp
                n=n//10
            return self.isHappy(sum) 
