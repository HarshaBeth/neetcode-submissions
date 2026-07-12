class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base case
        if len(nums) == 1:
            return [nums[:]]
        

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            # Append the popped first number to the end of the permute found
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        
        return result