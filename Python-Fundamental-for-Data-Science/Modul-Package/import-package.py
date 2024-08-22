#1. Import Package dan Menggunakan modul
import math
print("Nilai pi adalah:", math.pi)  # math.pi merupakan sintak untuk memanggil fungsi pi

#2. Menggunakan m sebagai module rename atau alias
import math as m
#m.pi merupakan sintak untuk memanggil fungsi
print("Nilai pi adalah:", m.pi)

#3 Import sebagaian fungsi
from math import pi
print("Nilai pi adalah", pi)

#Import semua isi Modulus
from math import *
print("Nilai e adalah:", e)