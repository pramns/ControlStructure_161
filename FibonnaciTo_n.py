n = int(input("Masukan Jumlah suku (n) = "))
a, b = 0, 1
print ("Deret Fibonnaci = ", end=" ")
for i in range(n) :
  print (a , end=" ")
  a, b = b, a + b 
  print(end=" ")