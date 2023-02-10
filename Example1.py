def Silnia(n):
    if (n == 1):
        return 1
    return n * Silnia(n-1)

x = 6
f = Silnia(x)
print(x, f)