def sumFunc(a,d,n):
    if n == 1:
        return a
    else:
        return a + (n-1)*d + sumFunc(a,d,n-1)

a = int(input('Enter the first element of series: '))
n = int(input('Number of Elements to Calculate the Sum: '))
d = int(input('Interval among consecutive numbers: '))
result = sumFunc(a,d,n)
print('The sum is: ', result)





