def deep_copy(l):
 m=[]
 for i in l: 
  if (type(i)==list):
   m.append(deep_copy(i))
  else:
   m.append(i)
 return m
l=[[1,2],[3,4]]
k=deep_copy(l)
print k,l
k[0][1]=1
print k,l

