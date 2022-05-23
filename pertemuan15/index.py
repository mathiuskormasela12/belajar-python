# Error Handling

# A. Raise
# Raise akan memtikan program dan memberi pesan error custom
# raise 'Yah error'


# B. Try Except
#v try except sederhana
# try :
# 	print('Behasil' + s)
# except: 
# 	print('ada error bre')

# try except dengan beberapa NameError (Jika erronya berkaitan dengan nama variable, misak variable nya namanya salah atau gk ada)
# try :
# 	print(nama)
# except NameError:
# 	print('NameError bre, nama variablenya tidak di temukan')

# try except dengan Value Error (jika ada masalah dengan valuenya)
# a = 10
# try :
# 	print(a + '10')
# except ValueError :
# 	print("ValueError bre, nilai variablenya bermasalah")

# C. assert

import sys

assert('linux' in sys.platform), 'ini hanya untuk linux'

print(sys.platform)