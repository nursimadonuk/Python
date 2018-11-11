prefixes = "JKLMNOPQ"
suffix = "ack"
suffix2 = "uack"

for p in prefixes:
    if p == "O" or p == "Q":
        print(p + suffix2)
    else:
        print(p + suffix)
