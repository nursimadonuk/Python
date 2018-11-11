def sumUntilEven(lst):
    i = 0
    sum = 0 
    while i < len(lst) and lst[i] % 2 == 1:
        sum += lst[i]
        i += 1
    return sum
        
print(sumUntilEven([1,2,3,4,5]))
print(sumUntilEven([1,3,5,7,9]))
print(sumUntilEven([2,4,6,7,9]))

