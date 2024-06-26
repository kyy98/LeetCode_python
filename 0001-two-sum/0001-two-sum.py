#브루트 포스
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]

#in 이용 탐색
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n in enumerate(nums):
#             complement = target-n

#             if complement in nums[i+1:]:
#                 return [nums.index(n), nums[i+1:].index(complement)+(i+1)]

#첫 번째 수를 뺀 결과 키 조회
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_map = {}
#         for i, num in enumerate(nums):
#             nums_map[num] = i
#         for i, num in enumerate(nums):
#             if target-num in nums_map and i!= nums_map[target-num]:
#                 return [i, nums_map[target-num]]

# 조회 구조 개선
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_map = {}

#         for i, num in enumerate(nums):
#             if target-num in nums_map:
#                 return [nums_map[target-num], i]
#             nums_map[num] = i

##투포인터
##[3,2,4] 경우 실행 안됨
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start, end = 0,len(nums)-1

        while start != end:
            if nums[start] + nums[end] < target:
                start+=1
            elif nums[start] + nums[end] > target:
                end-=1
            else:
                return [start, end]




        
