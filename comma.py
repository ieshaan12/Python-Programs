def comma(l):
    S=l[0]
    for i in range(1,len(l)-1):
        S+=', '
        S=S+l[i]
    S+=' and '+l[-1]
    return S
l=['cats','apps','bananas','monkeys','dogs']
print(comma(l))
        
