def palind(r):
    e =len(r) - 1
    s = 0
    while s<e:
        if (r[s]!=r[e]):
            return False
        e-=1
        s+=1
    return True


r = (7, 3, 8, 4, 6, 7)
if palind(r):
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")

