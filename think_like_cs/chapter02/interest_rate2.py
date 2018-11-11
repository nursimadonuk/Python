#this code will calculate the final amount if one is earning compound interest
#where p is the principal amount, n is the number of times it will bw compounded in a year
#t is the number of years and r is the interest rate
t = int(input("what is the number of years the money will be compounded for?"))
P = 10000
n = 12
r = 0.08
A= P*(1+(r/n))**(n*t)
print ( "the final amount after", t, "years would be", A)
