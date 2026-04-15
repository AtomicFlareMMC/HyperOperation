def HyperOperation(a,level,b):
    if a<=0 or level<=0 or b<=0:
        print("Input Error")
        return 0
    if level==1:
        return a**b
    if b==1:
        return a
    return HyperOperation(a,level-1,HyperOperation(a,level,b-1))

print(HyperOperation(3,1,3))    
print(HyperOperation(3,2,3))
print(HyperOperation(3,2,2))