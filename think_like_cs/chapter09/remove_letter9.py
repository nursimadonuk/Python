def remove_letter(theLetter, theString):
    newString = ""
    for letter in theString:
        if letter == theLetter:
            newString = newString
        else:
            newString += letter
    return newString

print(remove_letter( 'a', 'bannana'))