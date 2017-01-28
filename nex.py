import sys
global s
s=[0]
c=lambda x: x.append(str(x.pop())+str(x.pop()))
i=lambda x: x.append(x.pop()+1)
v=lambda x: x.append(x.pop()-1)
x=lambda x: x.append(x.pop()*x.pop())
q=lambda x: x.append(x.pop(-2)/x.pop())
a=lambda x: x.append(x.pop()+x.pop())
w=lambda x: x.append(x.pop(-2)-x.pop())
e=lambda x: x.append(x.pop(-2)**x.pop())
m=lambda x: x.append(x.pop(-2)%x.pop())
r=lambda x: x.append(x.pop(0))
l=lambda x: x.insert(0,x.pop())
d=lambda x: x.append(x[-1])
t=lambda x: x.extend(x[-2:])
s=lambda x: x.insert(-2,x.pop())
def z(x):
    for y in [0,1]:
        s.insert(-2,s.pop())
k={'$':c,'i':i,'v':v,'*':x,'/':q,'+':a,'-':w,'^':e,'%':m,'>':r,'<':l,'d':d,
   't':t,'s':s,'z':z,'.': lambda x: x.pop()}
if __name__=='__main__':
    with open(sys.argv[1],'r') as f:
        while 1:
            b=f.read(1)
            if not b or b not in k.keys():
                break
            else:
                n=k[b](s)
                for x in s: print s,
