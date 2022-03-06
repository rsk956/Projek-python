def Persamaan(x):
	return (x**2)-x-6

def menu():
	try:
		a = int(input('Masukkan nilai a\t: '))
		b = int(input('Masukkan nilai b\t: '))
		n = int(input('Jumlah iterasi\t\t: '))
		print('')

		if(n>0):
			fa = Persamaan(a)
			fb = Persamaan(b)
			if(fa*fb>=0):
				print('Proses dihentikan karena tidak ada akar!!')
				pilih = str(input('Coba lagi?y/t->'))
				if(pilih == 'y'):
					print('')
					menu()
				else:
					print('')
					print('Program Berhenti')
			else:
				for i in range(n):
					c = (a+b)/2
					fc = Persamaan(c)
					print('Iterasi',i)
					print('a =',a,'\t->f(a)=',fa)
					print('b =',b,'\t->f(b)=',fb)
					print('c =',c,'\t->f(c)=',fc)
					print('')
					if(fc<0):
						a = c
						fb = fc
					else:
						b = c
						fa = fc
	except:
		print('Program hanya menerima inputan angka!\nMohon masukkan inputan yang benar\n')
		menu()

print('Carilah Persamaan dari f(x)=x^2-x-6')
menu()

