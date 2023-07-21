def gcd(a,b):
    if a %b==0:
        return b
    else:
        return gcd(b,a%b)

def lcm(a,b):
    hcf=gcd(a,b)
    return (hcf*(a//hcf)*(b//hcf))

a,b=eval(input("DIVIDEND , DIVISOR ="))
print(f"GCD of {a} and {b} is : {gcd(a,b)}")
print(f"LCM of {a} and {b} is : {lcm(a,b)}")