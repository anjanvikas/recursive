def fibonacci(n,a,b):
 if (n==1):
  return a
 k=a
 sum=a+b
 a=b
 b=sum
 sum=k+fibonacci(n-1,a,b)
 return sum
print fibonacci(8,1,1)
