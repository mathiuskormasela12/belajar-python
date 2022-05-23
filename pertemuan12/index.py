"""
	============ Belajar Function ============

	Function merupakan kumpulan block kode
	yang dapat di panggil berkali-kali.

	rumus :

	a. Function Tanpa Arguments/Parameters

	   def namaFunction() :
			 statement
	
	b. Function Dengan Arguments/Parameters

		 def namaFunction(namaArgument) :
			 statement

		ket :
		arguments/parameternya boleh lebih dari satu
	
	C. Function Dengan Return
	   def namaFunction() :
			 return statement

"""

# Function Tanpa Parameter
def sayHello() :
	print('Hello Python')

# memanggil function
sayHello()

# Function Dengan Parameter
def jikoshokai(nama, usia) :
	print('Halo nama saya ' + nama + ' saya berusia ' + str(usia) + ' tahun.')

jikoshokai('Mathius', 20)

# Function Dengan Return
def jikoshokai2(nama, usia) :
	return 'Hi, My name is ' + nama + ' and I am ' + str(usia) + ' years old.'

print(jikoshokai2('Matt', 21))

# Function Dengan Default Parameter
def test(nama = 'Matt') :
	print(nama)

test('tius')

def test2(nama, usia) :
	print('Saya adalah', nama)
	print('Saya berusia', usia)
	# memberinama pada parameter dengan  (jadi urutannya gk perlu terutur, ini argumentnys akan menjadi dictionary)
test2(usia = 26, nama = 'Dita')

"""
	Keywords *args berfungsi sama seperti
	rest parameter di Javasript. Kita gunakan
	jika kita tidak mengetahui suatu function
	akan memiliki berapa parameter atau jika
	parameternya itu dinamis. ini akan menghasilkan
	tipe data tupples.

	*args => args nya misa diganti kata lain misal *mathius
"""
def loop(*args) :
	for item in args :
		print(item)

loop(1, 2, 3, 4, 5)

"""
	Keywords **kwargs berfungsi sama seperti keyword *args
	namun khusus untuk *kwargs di parameternya bisa
	di kasihnama dan kwargs agan bertipe data dictionary
"""
def printData(**kwargs) :
	for key, value in kwargs.items() :
		print(key, '=>', value)

printData(name = 'Python', framework = 'FastAPI')