def recur(a,b):
 if (b==1):
  return a    
 mult=a*recur(a,b-1)
 return mult
def wfor(a,b):
 mult=1
 for i in range(b):
  mult=mult*a
 return mult
def wwhile(a,b):
 mult=1
 i=0
 while(i<b):
  mult=mult*a
  i=i+1
 return mult
print recur(2,10),wfor(2,10),wwhile(2,10)
