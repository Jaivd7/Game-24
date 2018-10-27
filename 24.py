import operator
a=input("Enter a Number ")
b=input("Enter a Number ")
c=input("Enter a Number ")
d=input("Enter a Number ")
l=[a,b,c,d,a,b,c,d,a,b,c,d,a,b,c,d]
op=[operator.add, operator.sub, operator.mul, operator.div]
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            for i in range(4):
                if op[i1](op[i2](op[i3](l[i], l[i+1]), l[i+2]), l[i+3])==24.00:
                    print '(((',l[i],op[i3],l[i+1],')',op[i2],l[i+2],')',op[i1],l[i+3],')'
                elif op[i1](op[i2](op[i3](l[i], l[i+1]), l[i+3]), l[i+2])==24.00:
                    print '(((',l[i],op[i3],l[i+1],')',op[i2],l[i+3],')',op[i1],l[i+3],')'
                elif op[i1](op[i2](op[i3](l[i], l[i+2]), l[i+1]), l[i+3])==24.00:
                    print '(((',l[i],op[i3],l[i+2],')',op[i2],l[i+1],')',op[i1],l[i+3],')'
                elif op[i1](op[i2](op[i3](l[i], l[i+2]), l[i+3]), l[i+1])==24.00:
                    print '(((',l[i],op[i3],l[i+2],')',op[i2],l[i+3],')',op[i1],l[i+1],')'
                elif op[i1](op[i2](op[i3](l[i], l[i+3]), l[i+2]), l[i+1])==24.00:
                    print '(((',l[i],op[i3],l[i+3],')',op[i2],l[i+2],')',op[i1],l[i+1],')'
                elif op[i1](op[i2](op[i3](l[i], l[i+3]), l[i+1]), l[i+2])==24.00:
                    print '(((',l[i],op[i3],l[i+3],')',op[i2],l[i+1],')',op[i1],l[i+2],')'
