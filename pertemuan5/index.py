# =============== Belajar Conversi Tipe Data ===============
# Dalam Python kita tidak bisa melakukan operasi aritmatika
# atau concatination antara number dan string. Oleh sebab
# itu kita harus menkonversinya.

# Konversi tipe data lain ke tipe data string
angka = 10
angka = str(angka)
print(type(angka))

# Konversi tipa data string ke number
x = '10.5'
print(float(x) + 2)
s = '10'
print(int(s) + 2)

# ini akan error
print(2 + '2')