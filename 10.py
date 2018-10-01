def adding(l):
 if (len(l)==1):
  return l[0]
 sum=l[0]+adding(l[1:])*10
 return sum

def dividing(x):
 l=[]
 if (x<10):
  return x
 remainder=x%10
 l.append(remainder)
 if (x<100):
  l.append(dividing(x/10))
 else:
  l.extend(dividing(x/10))
 return l

def next(l):
 x=adding(l[::-1])
 k=dividing(x+1)
 return k[::-1]

l=[1,2,3,4]
print next(l)

