def mirror(mystr):
    rvrse = reverse(mystr)
    newstr = mystr + rvrse
    return newstr
def reverse(mystr):
    newstr = ""
    for item in mystr:
        newstr = item + newstr
    return newstr
print(mirror('hello'))