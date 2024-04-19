# ex 1
# n = int(input())
def square(n):
    for i in range(0,n+1):
        yield i**2


# for i in square(n):
    # print(i)

# ex 2
# n = int(input())
def even(n):
    for i in range(0,n+1):
        if(i%2 == 0):
            yield i

# generator = even(n)
#for i in generator:
    # print(i)

# ex 3
# n = int(input())
def div_by_3_and_4(n):
    for i in range(1,n+1):
        if i % 12 == 0:
            yield i

# generator = div_by_3_and_4(n)
# for i in generator:
    # print(i)

# ex 4
# a = int(input())
# b = int(input())
def sq(a,b):
    for i in range(a,b+1):
        yield i**2
# square = sq(a,b)
# for i in square:
    # print(i)

# ex 5
# n = int(input())
def down(n):
    while(n > 0):
        n-=1
        yield n
# generator = down(n)
# for i in generator:
    # print(i)
























