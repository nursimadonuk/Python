def replace(s, old, new):
    l = list(s)
    new_l = []
    i = 0
    while i < len (l):
        if l[i] == old:
            l[i] = new
        new_l.append(l[i])
        i += 1
    new_s = "".join(new_l)
    return new_s

print(replace("Hello World", "o", "a"))
