class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def toDigit(num:str):
            dig = 0

            for c in num:                           # we are iterrating character  
                dig = dig * 10 + (ord(c) - ord("0"))   #ord stand for ordinal

            return (dig)

        return str(toDigit(num1) * toDigit(num2))

