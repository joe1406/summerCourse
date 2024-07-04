def max(x,y):
    if x > y:
        return f"{x} is bigger"
    elif x == y :
        return "they are equal"
    else:
        return f"{y} is bigger"
    
print(max(3,5))
print(max(234,13245))
print(max(2,2))