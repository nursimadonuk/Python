#Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
  if nums[0] == 2 or nums[1] == 2:
    return True
  elif nums[0] == 3 or nums[1] == 3:
    return True
  else:
    return False

print(has23([8,9]))
print(has23([3,6]))
print(has23([9,2]))
print(has23([2,3]))


#Given an array of ints, return True if 6 appears as either the first or last element in the array.
#The array will be length 1 or more.
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False

print(first_last6([3,4,6,3,32,5]))
print(first_last6([6,32,1,223,7,8,0]))
print(first_last6([3,5,3,45,65,7,6]))

#Given an array of ints length 3, return a new array with the elements in reverse order,
##so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
  new_l=[]
  i = 0
  s = -1
  while i < len(nums):
    a = nums[s]
    new_l.append(a)
    i += 1
    s -= 1
  return new_l

print(reverse3([5,6,2]))
print(reverse3([4,9,1]))
print(reverse3([1,2,3,4,5,6,7,8,9]))

#Given 2 int arrays, a and b, each length 3,
#return a new array length 2 containing their middle elements.
def middle_way(a, b):
  new_l = []
  A = a[len(a)//2]
  B = b[len(b)//2]
  new_l = [A] + [B]
  return new_l

print(middle_way([1,2,3],[4,5,6]))
print(middle_way([7,7,7],[3,8,0]))
print(middle_way([5,2,9],[1,4,5]))









