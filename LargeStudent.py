a = int(input("Masukan Angka Pertama = "))
b = int(input("Masukan Angka Kedua = "))
c = int(input("Masukan Angka Ketiga = "))

if a > b and a > c :
  terbesar = a
elif b > a and b > c :
  terbesar = b
elif c > a and c > b :
  terbesar = c
else :
  print("Tidak ada Angka Terbesar")

print("Angka  Terbesar adalah =", terbesar)