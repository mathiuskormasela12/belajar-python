"""
	================ Belajar Tipe Data Boolean & Conditional ================

	A. Tipe Data Boolean
	   Tipe data boolean merupakan tipe data
		 yang hanya memiliki dua buah nilai, yaitu
		 True atau False (inget huruf depannya capital).
		 Tipe data ini biasanya kitak gunakan untuk pengkondisian.
		 Selain itu biasanya juga tipe data ini merupakan hasil
		 dari operator perbandingan.

		 contoh :
		 menikah = True
		 blmMenikah = False

	B. Conditional
	   Conditional berfungsi untuk melakukan pengkondisian.
		 Dalam Python Conditional terdiri atas if elif dan els.

		 Rumus :
		 if kondisi :
			 statement
		 elif kondisi :
			 statement
		 else :
			 statement
"""

# Membuat tipe data boolean
menikah = False
blmMenikah = True

age = '20m'

"""
	variable.isdigit() => untuk mengecek variable tersebut tipe datanya string angka atau bukan
	variable.isalnum() => untuk mengecek variable tersebut tipe datanya string alfa numeric atau bukan
"""

if age.isdigit() :
	print('Tipe datanya string number')
elif age.isalnum() :
	print('Tipe datanya string alfa numeric')
else :
	print('Tidak datanya tidak di kenali')