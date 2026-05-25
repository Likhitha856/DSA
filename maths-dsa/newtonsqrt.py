
n=37
def newtonrt(n,tolerance=1e-5):
    x=n/2
    while True:
        root=0.5*(x+(n/x))
        if abs(root-x)<tolerance:
            return round(root,4)
        x=root

print(newtonrt(n))