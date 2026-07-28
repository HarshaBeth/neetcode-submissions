class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                # Multiplication and adding existing digit
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                # Store current value and carry to the next index
                res[i1 + i2 + 1] += (res[i1 + i2] // 10) # Carry
                res[i1 + i2] = (res[i1 + i2] % 10) # Keep
                
        
        res, start = res[::-1], 0
        while start < len(res) and res[start] == 0:
            start += 1
        
        # Convert to string
        res = map(str, res[start:])
        return "". join(res)
