def twoSum(nums, target):
        num_to_index = {} # Map each number to its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                  return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

# Test Cases
# nums = [10, 15, 3, 7]
# target = 13
# print(twoSum(nums, target))
