add=lambda x,y:x+y
l=[7,8,1,2,3,4,5]
a=[3,4,1,29,1,5,1]
d=list(map(add,l,a))
print(d)
e=[4,1,69,2,7,3,6]
f=list(map(add,d,e))
print(f)
mul=lambda x,y:x*y
y=list(map(mul,d,f))
print(y)
