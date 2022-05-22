"""
	=========== Belajar Operator Perbandingan & Operator Logika ===========

	A. Operator Perbandingan
	   == (operator sama dengan)
		 != (operator tidak sama dengan)
		 < (operator lebih kecil dari)
		 > (operator lebih besar dari)
		 <= (operator lebih kecil dari sama dengan)
		 ?= (operator lebih besar dari sama dengan)

	B. Operator Logika
	   and (operator and)
		 or (operator or)
		 not (operator negasi)

	C. Operator Bitwise (agar hasilnya akurat ketika melakukan perbandingan usahakan gunakan tanda ())
	   & (operator and)
		 | (operator atau)
		 ~ (operator negasi)
"""

x = 10
y = 5

# Kalau kita gk oake tanda () maka hasil nya adalah 'salah'
if (x == 10 ) & (y == 5) :
	print('benar')
else :
	print('salah')

# Jika kita gk pengen pake tanda () kita bisa paka operator logika
if x == 10  and y == 5 :
	print('benar2')
else :
	print('sala2')


menikah = False

if(~menikah) :
	print('sudah menikah')
