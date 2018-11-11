def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price > 0:
            if price == 0:
                print ('Error: the first vaue cannot be zero')
            else:
                count = count + 1
                total = total + price
                print('Subtotal: $', total)
        elif price < 0:
            print ('Error: price cannot be negative.')
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()