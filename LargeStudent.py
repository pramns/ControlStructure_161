a = int(input("Masukan Angka Pertama = "))
b = int(input("Masukan Angka Kedua = "))
c = int(input("Masukan Angka Ketiga = "))

if a >= b and a >= c :
  terbesar = a
elif b >= a and b >= c :
  terbesar = b
else :
  terbesar = c

print("Angka  Terbesar adalah =", terbesar)