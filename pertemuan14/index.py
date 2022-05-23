# Belajar Built-in module datetime
import datetime

# mencetak waktu sekarang
print(datetime.datetime.now())

# mencetak waktu custom
print(datetime.datetime(2001, 10, 4))

# formating
dob = datetime.datetime(2001, 10, 4)
print('Saya lahir pada', dob.strftime('%A, %d %B %Y'))