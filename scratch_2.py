print("Program Menghitung Linear Programming secara Manual \n"
      "Optimalisasi keuntungan dari supplier yang berbeda")

print("Memiliki kriteria sbg berikut : ")
print("| Kriteria     |  Supplier  |")
print("|              |  A  |  B   | Batasan |")
print("| Jarak      : | 10  |  15  |   70    |")
print("| Waktu      : | 03  |  04  |   20    |")
print("| Keuntungan : | 100 |  120 |\n")


#Definisi Jarak beserta batasannya
j1 = 10
j2 = 15
a = 70

#Cari x dan y jarak
ax = a/j1
ay = a/j2

#Definisi Waktu beserta batasannya
w1 = 3
w2 = 4
b = 20

#Cari x dan y waktu
bx = b/w1
by = b/w2

#Cari Titik tengah
t1 = j1*w1 - w1*j1
t2 = j2*w1 - j1*w2
t3 = w1*a - j1*b
t4 = int(t3/t2)
t5 = w2*t4
t6 = b - t5
t7 = int(t6/w1)

print(f'{j1}A + {j2}B ≤ {a}')
print(f' {w1}A +  {w2}B ≤ {b}')
print("---------------")
print(f'{j1*w1}A + {j2*w1}B ≤ {w1*a}')
print(f'{j1*w1}A + {j1*w2}B ≤ {j1*b}')
print("---------------")
print(f'       {t2}B = {t3}')
print(f'        B = {int(t4)}')
print("---------------")
print(f'{w1}A + {w2}B ≤ {b}')
print(f'{w1}A + {w2}({t4}) ≤ {b}')
print(f'{w1}A + {t5} ≤ {b}')
print(f'{w1}A = {b} - {t5}')
print(f'{w1}A = {t6}')
print(f'A = {t6} : {w1}')
print(f'A = {int(t7)}')

print(f'maka didapatkan titik 3 memiliki x = {t4} dan y =  {t7}\n')

k1 = 100
k2 = 120
#Menghitung Titik 1,2,3,4
t8 = k1*0 + k2*0
t9 = k1*0 + k2*ay
t10 = k1*t4 + k2+t7
t11 = k1*bx + k2*0
print("maka didapatkan 4 titik yaitu ")
print(f'titik 1 = {k1}*0 + {k2}*0 = ', int(t8))
print(f'titik 2 = {k1}*0 + {k2}*{int(ay)} = ', int(t9))
print(f'titik 3 = {k1}*{int(t4)} + {k2}*{int(t7)} = ', int(t10))
print(f'titik 4 = {k1}*{int(bx)} + {k2}*0 = ', int(t11))
print(f'maka didapatkan titik yang memiliki titik terbesar yaitu {int(t11)} ')