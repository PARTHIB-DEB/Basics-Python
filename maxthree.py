a,b,c=eval(input("Enter 3 numbers(a,b,c):"))
def max_three(a,b,c):
    my_tup=(a,b,c)
    return max(list(my_tup))
print(max_three(*(a,b,c)))
