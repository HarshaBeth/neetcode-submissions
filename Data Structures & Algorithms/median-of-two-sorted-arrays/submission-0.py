class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 == 0:
            idx1 = (len(nums) // 2) - 1
            idx2 = idx1 + 1

            return (nums[idx1] + nums[idx2]) / 2
        else:
            idx = len(nums) // 2

            return nums[idx]
        

