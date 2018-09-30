def recur(n):
 if (n==1):
  return 1
 mult=n*recur(n-1)
 return mult
def wfor(n):
 mult=1   
 for i in range(1,n+1):
  mult=mult*i
 return mult
def wwhile(n):
 mult=1
 i=1
 while(i<n+1):
  mult=mult*i
  i=i+1 
 return mult
print recur(5),wfor(5),wwhile(5)
