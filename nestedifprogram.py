a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print("{} is greatest".format(a))
    else:
        print("{} is greatest".format(c))
else:
    if b>c:
        print("{} is greatest".format(b))
    else:
        print("{} is greatest".format(c))