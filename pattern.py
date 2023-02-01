#half diamond pattern

r=int(input("enter the number of rows:"))
for i in range(1,r):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(r,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()


# diamond shape pattern
r=int(input("enter the number of rows:"))
for i in range(r):
    print(' '*(r-i-1)+" *"*(i+1))
for j in range(r-1,0,-1):
    print(' '*(r-j)+" *"*(j))



#pascals triangle