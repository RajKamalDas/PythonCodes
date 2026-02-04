def myfunc(n,CloseTo):
  return abs(n - CloseTo) #<- sorts as the closest to 50.

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc(n=thislist,CloseTo=50))

print(thislist)