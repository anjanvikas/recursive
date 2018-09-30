def recur(l):
 if (len(l)==1):
  return l[0]
 sum=l[0]+recur(l[1:])
 return sum
def wfor(l):
 sum=0
 for i in l:
  sum=sum+i
 return sum
def wwhile(l):
 i=0
 sum=0
 while(i<len(l)):
  sum=sum+l[i]
  i=i+1
 return sum
l=[1,2,1,2,3]
print recur(l),wfor(l),wwhile(l)
