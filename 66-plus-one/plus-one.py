class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one , i =1,0
        digit = digits[::-1]

        while one:
            if i < len(digit):
                if digit[i] == 9:
                    digit[i] = 0
                else:
                    digit[i] += 1
                    one = 0
            else:
                digit.append(1)
                one = 0

            i+=1

        return digit[::-1]