def count():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = input('enter your text')
    letter = input('pick a letter')
    letter = letter.lower()
    count = 0
    lttrcnt = 0
    for ch in text.lower():
        if ch == letter:
            lttrcnt += 1
            count += 1
        elif ch == " ":
            lttrcnt = lttrcnt
            count = count
        else:
            count +=1
    return 'your text contains ' + str(count) + ' alphabetic charecters,of which ' + str(lttrcnt) + ' ( approximetely ' + str(lttrcnt*100//count) + ' %) are the letter ' + str(letter)
print (count())     
