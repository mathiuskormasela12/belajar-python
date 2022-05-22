"""
	=============== Belajar Looping ===============

	A. While Loop
	   Berfungsi untuk melakukan perulangan.

		 rumus :

		 while kondisi :
			 statement
			 increment/decerement
		 else :
			 statement yg akan di jalankan ketika looping sudah berhenti
	
	B. For In
	   Berfungsi untuk melooping list atau string

		 for namaVariable in namaList :
			 statement
"""

# While Loop
count = 1

while count <= 5 :
	print('Perulangan ke-', count)
	count += 1
else :
	# akan disajalankan ketika perulangan berenti atau ketika kondisinya sudah tidak terpenuhi
	print('Yeah, perulangan telah perhenti')

print('')
print('===================')
print('')

# Membuat list atau array
skills = ['HTML', 'CSS', 'Javascript', 'Node Js', 'MySQL', 'MongoDB', 'Express Js', 'Next Js']

for skill in skills :
	print(skill)

print('')
print('===================')
print('')

# Melooping angka dengan for in
# melooping sebanyak 4 kali, dari angka 1 sampai angka 5
for angka in range(1, 5) :
	print('Perulangan ke-', angka)