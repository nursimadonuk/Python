"""
given a list and a sum
check if there is a pair of numbers in that list
that add up to the given sum
if yes return True and maybe the pair
if no reurn False
"""

def check_for_pair(l, num):
    n = False
    i = 0
    j =-1
    for a in l:
        if l[i] + l[j] == num:
            lt = ([l[i]] + [l[j]])
            print (lt)
            n = True
            j -= 1
            i += 1
        elif l[i] + l[j] > num:
            j -= 1
        elif l[i] + l[j] < num:
            i += 1
    return n
    
print(check_for_pair([1,2,3,4,5,6,7,8,9] , 17))
print(check_for_pair([1,2,3,4,5,6,7] , 1))
print(check_for_pair([1,2,3,4,5,6], 10))
print(check_for_pair([1,2,3,4,5,5,6,7,8,9], 10))
print(check_for_pair([1,2,3,7,8,9,10], 11))
            