def subset_sum(nums, target, i=0):
    if target == 0: return True
    if i == len(nums) or target < 0: return False
    return subset_sum(nums, target-nums[i], i+1) or subset_sum(nums, target, i+1)

def partition(nums):                      # Partition reduction
    s = sum(nums)
    return (s % 2 == 0) and subset_sum(nums, s//2)

nums = [3, 1, 5, 9, 12]
target = 9

print("Subset Sum:", subset_sum(nums, target))
print("Partition Possible:", partition(nums))
