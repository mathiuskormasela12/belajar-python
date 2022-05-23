"""
	============= Belajar Sequence =============

	A. List
	   List merupakan tipe data yang memungkinkan
		 value nya lebih dari satu dan berbeda-beda
		 tipe datanya. Tipe data ini adalah tipe data array
		 kalau di Javascript.

		 rumus :
		 namaList = [value, value, value]
	
	B. Tupples
	   Tupple merupakan tipe data yang mirip dengan
		 list namun dia bersifat immutable, jadi kita
		 tidak bisa menghapus, menambah atau mengedit item-itemnya.

		 rumus :
		 namaTupple = (value, value, value)
	
	C. Dictionary
	   Dictionary merupakan tipe data key value seperti 
		 object di Javascript atau assosiatif array di PHP.

		 rumus :
		 namaDictionary = {
			 key: value,
			 key: value
		 }

	D. Sets
	   Sets merupakan tipe data yang memiliki value lebih dari satu
		 namun dia tidak memiliki urutan dan tidak boleh memiliki
		 item yang duplicate, jika ada otomatis item nya salah satu nya
		 akan di hapus.

		 rumus :
		 namaSets = {value, value, value}
"""

# A. List
skills = ['Javascript', 'Typescript', 'Python']
# menampilkan semua element list
print(skills)
# menampilkan element list
print(skills[2])
#menambah element list
skills.append('Go')
print(skills)
# mengedit elemeent list
skills[3] = 'Golang'
print(skills)
# menghapus element list
del skills[3]
print(skills)
# menampilkan seluruh element list dengan looping
for item in skills :
	print(item)


# B. Tupples
data = ('HTML', 'CSS')
# menampilkan semua element tupples
print(data)
# menampilkan element tupples
print(data[0])
# menampilkan item tupple, list dan sets yg jumlah karakternya terbesar dan terkecil
print(max(data))
print(min(data))

# C. Dictionary
mhs = {
	'nama': 'Mathius',
	'usia': 20
}
# menampilkan semua datanya
print(mhs)
# menampilkan nama
print(mhs['nama'])
# menambahkan key
mhs['asal'] = 'Jakarta'
print(mhs)
# mengubah key
mhs['asal'] = 'Seoul'
print(mhs)
# menghapus key
del mhs['asal']
print(mhs)
# menampilkan key dan value dengan looping
for key, value in mhs.items() :
	print(key, ' = ', value)

# D. Sets
orang = {'budi', 'arya', 'siti'}
# menampilkan semua element sets
print(orang)
# menambah sebuah element sets
orang.add('alex')
# menghapus element set
orang.remove('budi')
print(orang)

angka1 = {1, 2, 3, 4, 5}
angka2 = {4, 5, 6, 7, 8}
# operator relasi di MTK (menggabungkan semua element dan kalau ada yg sama tampilin sekali)
print(angka1 | angka2)
# operator intersection atau irisan di MTK
print(angka1 & angka2)
# operator difference atau perbedaan di MTK (menampikan element angka1 yg gk ada di angka2)
print(angka1 - angka2)
# operator untuk mencari item yg gk kembar di angka1 dan angka2
print(angka1 ^ angka2)

# nested
x = [[1, 2]]
print(x[0][1])
a = ((1, 2), (3, 4))
print(a[0][1])
b = {
	"data": {
		"nama": "mathius"
	}
	}
print(b['data']['nama'])