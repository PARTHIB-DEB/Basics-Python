def swap_without_3rd(a,b):
    a,b=b,a
    return (a,b)
a,b=eval(input("a,b="))
(a,b)=swap_without_3rd(a,b)
print("a = %d,b = %d" % (a,b))