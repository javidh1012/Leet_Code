class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumofsquare(n)

            if n == 1:
                return True
        return False

    def sumofsquare(self, n: int) -> int:
        op = 0
        while n :
            digit = (n % 10)**2
            op +=digit
            n = n //10
        return op

