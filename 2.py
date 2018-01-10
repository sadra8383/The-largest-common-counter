n=int(input())
h=int(input())
o=n%h
s=h
if o!=0:
    while s%o!=0:
        s=o
        o=h%o
print(o)
print("if it print 0 it means your smaler number is the answer")

        
    
