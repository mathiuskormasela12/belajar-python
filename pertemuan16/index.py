"""
	=========== Belajar Global & Local Variable ===========

	A. Global Variable
	   Global Variable adalah variable yg di buat
		 di luar suatu blok kode. (kalau di python itu, indentasi)
	B. Local Variable 
	   Local Variable merupakan variable yg di buat
		 di dalam suatu blok kode. (kalau di python itu, indentasi)
		 Contohnya variable di dalam function, if statement.
"""

# Global Variable
nama = 'Mathius'

def show() :
	# Local Variable
	# usia = 21
	# print(usia)
	# print(nama)

	# jika di dalam suatu function 
	# nama variable nya sama dengan 
	# yg di global, tpi kita ingin 
	# mengakses variable global nya 
	# kita bisa pake keyword global.
	# kita harus mendegfinisikan keyword global
	# di bagian pertama function
	global nama 
	nama = nama + ' test'
	print(nama)


show()
print(nama)
