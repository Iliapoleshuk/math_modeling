a = int(input())
m = 1
n = 2
l = 0
print(end=" ", l , m , n)
for i in range(4,a+1):
  print(m + n , end=" ")
  c = m
  m = n
  n = c + m
  

  
