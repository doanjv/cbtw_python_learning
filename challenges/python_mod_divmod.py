
def divmod(a, b):
    if(b==0):
        raise("The divisor should not be 0")
    result=int(a/b)
    mod = a%b
    print(f"{result}\n{mod}\n({result}, {mod})")
divmod(177, 10)