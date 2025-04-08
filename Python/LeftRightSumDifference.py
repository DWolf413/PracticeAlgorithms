class Solution:
    def findDifferenceArray(self, nums):
        
        n = len(nums)
        differenceArray = [0] * n

        leftSum = 0
        rightSum = sum(nums)

        for i in range(n):
            rightSum -= nums[i]
            differenceArray[i] = abs (leftSum - rightSum)
            leftSum += nums[i]  

        return differenceArray

       


if __name__ == '__main__':
    
    solution = Solution()
    print(solution.findDifferenceArray([1,1,1,1]))
    