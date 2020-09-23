def g_inverse(n):
    if n == 0:
        return (0, 0)
    elif n == 1:             
        return (1, 0)
    else:
        x, y = g_inverse(n-1)
        if x == 0:
            return (y+1, 0)
        else:
            return (x-1, y+1)


n = int(input("Enter value for n : "))


print("x(" + str(n) + ") vaut " + str(g_inverse(n)[0]) + " et y(" + str(n) + ") vaut " + str(g_inverse(n)[1]) + ".")