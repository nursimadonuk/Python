def common_end(a, b):
  if a[-1] == b[-1] or a[0] == b[0]:
    return True
  else:
    return False

print (common_end([1, 2, 3], [1, 3, 5, 7, 9]))
print (common_end([2, 4, 6, 8 ], [4, 8]))
print(common_end([3, 6, 9, 12, 15, 19], [2, 4, 8, 5]))