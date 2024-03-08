import time,math
# ex 1
# a = [1,2,3]
def multiply(a):
    sum = 1
    for i in a:
        sum = sum* i
    print(sum)

# multiply(a)

# ex 2
# s = str(input())
def cnt(s):
    cntl = 0
    cntr = 0
    for i in s:

        if i.islower():
            cntl += 1
        elif i.isupper():
            cntr += 1

    print(cntl)
    print(cntr)
# cnt(s)

# ex 3
# s = str(input())
def pal(s):
    l = 0
    a = len(s)
    r = a-1
    t = True
    while l<r:

        if(s[l] != s[r]):
            t = False
            print("Not Palindrome")
            break
        else:
            l += 1
            r -= 1
    if t:
        print("Palindrome")

# pal(s)

# ex 4
# n,m = int(input()), int(input())
def mil(n,m):
    sec = m/1000
    time.sleep(sec)
    print(math.sqrt(n))
# mil(n,m)

# ex 5
tup = (1,2,'asd','yu',0)
def g(tup):
    for i in tup:
        if not i:
            return False
    return True
print(g(tup))


