#hallo selamat datang
g_ = "\033[32;1m"
gt_ = "\033[0;32m"
bt_ = "\033[34;1m"
b_ = "\033[36;1m"
m_ = "\033[31;1m"
c_ = "\033[0m"
p_ = "\033[37;1m"
u_ = "\033[35;1m"
M_ = "\033[3;1m"
k_ = "\033[33;1m"
kt = "\033[0;33m"
a_ = "\033[30;1m"

W = "\x1b[0m"
R = "\x1b[31m"
G = "\x1b[1;32m"
O = "\x1b[33m"
B = "\x1b[34m"
P = "\x1b[35m"
C = "\x1b[36m"
GR = "\x1b[37m"

import time
import sys
import os
os.system("clear")
def slow(s):
 for c in s:
  sys.stdout.write(c)
  sys.stdout.flush()
  time.sleep(5.0/90)
def slow1(s):
 for c in s:
  sys.stdout.write(c)
  sys.stdout.flush()
  time.sleep(1.0/90)
def slow2(s):
 for c in s:
  sys.stdout.write(c)
  sys.stdout.flush()
  time.sleep(2.0/90)
def slow3(s):
 for c in s:
  sys.stdout.write(c)
  sys.stdout.flush()
  time.sleep(3.0/90)
def slow4(s):
 for c in s:
  sys.stdout.write(c)
  sys.stdout.flush()
  time.sleep(4.0/90)
def slow5(s):
 for c in s:
  sys.stdout.write(c)
  sys.stdout.flush()
  time.sleep(9.0/90)


logo = (g_+'''
 _____        _                _  
|  ___|__ _  (_)  ___   __ _  | | 
| |_  / _` | | | / __| / _` | | | 
|  _|| (_| |_| |_\__ \| (_| |_| | 
|_| (_)__,_(_)_(_)___(_)__,_(_)_| 
''')
slow1 (logo)
slow1 (p_+'''\n   "MENEBAK TANGGAL LAHIR"''')
slow1 ("\n{ Author : faisal ramadhan              }")
slow1 ("\n{ Pesan : berdiri sejak tidak ada kursi }\n\n")
slow3 ("\n    [ LOADING ")
slow5 (". . . . . . ]")

slow ("\nHallo My Friend!\nKali ini Saya akan mencoba menebak tanggal lahir Anda.")

slow ("\nOKEY!\nPertama-tama kalikan tanggal lahir Anda dengan 5,\nContoh : 18x5= 90, kemudian masukan hasilnya di bawah!\n\n\n")

umur1 = int(input("Silahkan masukan hasil dari tanggal lahir anda yg sudah di kalikan dengan 5.\nJawab : "))
a = 5
b = (umur1/a)
c = (b*a)
if (umur1 == c):
 slow5 (g_+"..........OKE"+p_)
else:
 slow (g_+"....."+m_+".....GVLK")
 exit()

umur2 = int(input("\n\nKemudian tambah dengan 6.\nJawab : "))
d = 6
e = (c+d)
if (umur2 == e):
 slow (g_+"..........OKE"+p_)
else:
 slow (g_+"....."+m_+".....GVLK")
 exit()

umur3 = int(input("\n\nKemudian hasilnya dikalikan dengan 4.\nJawab : "))
f = 4
g = (e*f)
if (umur3 == g):
 slow (g_+"..........OKE"+p_)
else:
 slow (g_+"....."+m_+"......GVLK")
 exit()

umur4 = int(input("\n\nLalu hasilnya lagi tambahkan dengan 9.\nJawab : "))
h = 9
i = (g+h)
if (umur4 == i):
 slow (g_+"..........OKE"+p_)
else:
 slow (g_+"....."+m_+".....GVLK")
 exit()

umur5 = int(input("\n\nKemudian kalikan dengan 5.\nJawab : "))
j = 5
k = (i*j)
if (umur5 == k):
 slow (g_+"..........OKE"+p_)
else:
 slow (g_+"....."+m_+".....GVLK")
 exit()

umur6 = int(input("\n\nHasilnya tambahkan dengan bulan kelahiran anda.\nJawab :"))
l = 12
m = (k+l)
if (umur6 < m):
 slow (g_+"..........OKE KAWAN!!"+p_)
else:
 slow (g_+"....."+m_++".....GVLK")
 exit()

umur7 = 165
umur8 = (umur6)
hasil = (umur8-umur7)
s = str(hasil)
y = 1000
z = 0
x = str(z)
yz = (x+s)
slow4 ("\n\nSaya akan menganalisa sekarang\nMOHON TUNGGU")
slow5 ("......................\nSELESAI!!")
if (hasil < y):
 slow3 ("\ntanggal lahir Anda adalah     : "+yz[0:2])
 slow3 ("\ndan bulan lahir Anda adalah   : "+yz[2:4])
else:
 slow3 ("\ntanggal lahir Anda adalah     : "+s[0:2])
 slow3 ("\ndan bulan lahir Anda adalah   : "+s[2:4])


slow ("\nTerima kasih mencoba script ini/nSemoga hari anda menyenangkan :)")
