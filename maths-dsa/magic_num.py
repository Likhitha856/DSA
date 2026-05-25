def magic(n):
    result=0
    for i in range(32):
        if n>>i & 1:
            result+=5**(i+1)
    return result

print(magic(6))
