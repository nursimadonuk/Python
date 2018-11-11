def big_diff(nums):
  i=0 
  current_smallest = nums[0]
  current_largest =nums[0]
  while i <len(nums):
    if nums[i] < current_smallest:
      current_smallest = nums[i]
    if nums[i] > current_largest:
      current_largest = nums[i]
    i += 1
  return current_largest - current_smallesti