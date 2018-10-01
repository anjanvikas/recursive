def fraction(n):
 num=2
 while(num>0):
  if (num-n<0 and (num*2)-n>0):
   if (n-num>(num*2)-n):
    return float(n)/float(num*2)
   else:
    return 1-float(num)/float(n)
  else:
   num=num*2
  
   
   
def log2(n):
 count=0   
 if (n<2):
  return 0
 if (n%2==0):
  count=1+log2(n/2)
 else:
  count=log2(n-1)
 return count
n=input()
print log2(n)+fraction(n)
