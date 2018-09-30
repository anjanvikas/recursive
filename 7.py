def mymax(l):
 max=l[0]
 if(len(l)==1):
  return max
 if (max>mymax(l[1:])):
  max=max
 else:
  max=mymax(l[1:])
 return max
print mymax([4,1,3,2,5,6])
