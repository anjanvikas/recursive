def recur(a,b,i):
 if (a%i==0 and b%i==0):
  return i
 else:
  gcd=recur(a,b,i-1)
 return gcd
def wfor(a,b):
 for i in range(a):
  if (a%(a-i)==0 and b%(a-i)==0):
   return a-i
def wwhile(a,b):
 i=0
 while(i<a):
  if (a%(a-i)==0 and b%(a-i)==0):
   return a-i
  i=i+1
a=input()
b=input()
print recur(min(a,b),max(a,b),i=min(a,b)),wfor(min(a,b),max(a,b)),wwhile(min(a,b),max(a,b))
