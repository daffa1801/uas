import sqlite3
import subprocess as sp
#alasan menggunakan id untuk update dan
# hapus data adalah untuk menghindari error yang terjadi pada program sebelumnya 
# di mana program error di karenakan ada data npm yang sama program errror
#maka dari itu di sini kami menggunakan id di mana id tersebut di buat otomatis jadi tidak akan terjadi error
#akibat terjadinya 2 data primary key yang sama

#fungsi untuk membuat tabel baru
def buat_tabel():
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    CREATE TABLE IF NOT EXISTS data(
	    	id INTEGER PRIMARY KEY, 
	    	nama TEXT, 
	    	jurusan TEXT,
	        npm INTEGER
	    )
	'''

	cursor.execute(query)

	conn.commit()
	conn.close()


#fungsi untuk menambahkan data
def tambah_data_mhs(nama,jurusan,npm):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    INSERT INTO data( nama,jurusan,npm)
	    	        VALUES ( ?,?,? )
	'''

	cursor.execute(query,(nama,jurusan,npm))

	conn.commit()
	conn.close()


#fungsi untuk mencari data
def cari_data_mhs():
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    SELECT id,nama,jurusan
	    FROM data
	'''

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows
#fungsi untuk cari data by id/baris data sebelum di hapus
def cari_data_id(id):
	conn = sqlite3.connect('db')
	cursor = conn.cursor()
	query = '''
		select nama,jurusan,npm
		from data
		where id = {}'''.format(id)
	cursor.execute(query)
	all_rows = cursor.fetchone()

	conn.commit()
	conn.close()

	return all_rows

#fungsi untuk mencari nama pada baris untuk di tampilkan 
def cari_nama(nama):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    SELECT nama,jurusan,npm
	    FROM data
	    WHERE npm = {}
	''' .format(nama)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows
#fungsi untuk mengubah data
def ubah_data(nama,jurusan,npm,id):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()
	if nama == "" and jurusan != "":
		query = '''
		    update data data
		    SET jurusan = '{}', npm = {}
		    WHERE id = {}
		'''.format(jurusan,npm, id)
	elif nama == "" and jurusan == "" :
		query = '''
		    update data data
		    SET  npm = {}
		    WHERE id = {}
		'''.format(npm, id)
	elif nama != "" and jurusan == "":
		query = '''
		    update data data
		    SET nama = '{}', npm = {}
		    WHERE id = {}
		'''.format(nama,npm, id)
	elif nama != "" and jurusan != "":
		query = '''
		    update data
		    SET nama = '{}', jurusan = '{}', npm = {}
		    WHERE id = {}
		'''.format(nama,jurusan,npm, id)

	cursor.execute(query)

	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()
	print (all_rows)

#fungsiyang berguna untuk menampilkan data yang di cari
def tampilkan_data_cari(id_):
	students = cari_nama(id_)
	if not students:
		print("data tidak ada!!",id_)
	else:
		cursor.execute(query,(nama,jurusan,npm))

		conn.commit()
		conn.close()

#fungsi untuk menghapus data yang sudah ada
def hapus_data(id):
	conn = sqlite3.connect('db')

	cursor = conn.cursor()

	query = '''
	    DELETE
	    FROM data
	    WHERE id = {}
	''' .format(id)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows



buat_tabel()



"""
main code
"""


#fungsi yang di gunakan untuk memanggil fungsi yang sudah ada sebagai return
def tambah_data(nama,jurusan,npm):
	tambah_data_mhs(nama,jurusan,npm)
def tampil_data():
	return cari_data_mhs()
#fungsi untuk menampilkan data 
def tampil():
	students = tampil_data()
	head = ["id","nama","jurusan"]
	row_format ="|{:>5}" + ("|{:>30}" * (len(head) - 1))
	print(row_format.format(*head))
	for row in students:
		print("-"*120)
		print(row_format.format(*row))
#fungsi untuk menampilkan data yang di cari
def tampilkan_data_cari(id_):
	students = cari_nama(id_)
	if not students:
		print("data tidak ada!!",id_)
	else:
		print (students)

def tampil_by_id(id__):
	students = cari_data_id(id__)
	if not students:
		print("data tidak ada!!", id__)
	else:
		print(students)
def tampilkan_data_cari(id_):
	students = cari_nama(id_)
	if not students:
		print("data tidak ada!!",id_)
	else:
		print (students)
#fungsi untuk menampilkan menu utama
def menu():
	sp.call('cls',shell=True)
	sel = input("1.tambahkan data\n2.tampilkan data\n3.cari data\n4.update data\n5.hapus data\n6.Exit\n\n")

#if else untuk memilih menu	
	if sel=='1':
		sp.call('cls',shell=True)
		id_ = str(input('nama: '))
		name = str(input('jurusan: '))
		phone = str(input('npm : '))
		tambah_data(id_,name,phone)
	elif sel=='2':
		sp.call('cls',shell=True)
		tampil()
		input("\n\npress enter to back:")
	elif sel=='3':
		sp.call('cls',shell=True)
		id__ = int(input('masukan data npm : '))
		tampilkan_data_cari(id__)
		input("\n\npress enter to back:")
	elif sel=='4':
		sp.call('cls',shell=True)
		id__ = int(input('Enter Id(id data bisa di lihat di menu tampilkan data): '))
		tampil_by_id(id__)
		print()
		nama = str(input('nama: '))
		descrip = str(input('jurusan: '))
		npm = int(input('npm: '))
		ubah_data(nama,descrip,npm,id__)
		input("\n\ndata sudah di update \npress enter to back:")
	elif sel=='5':
		sp.call('cls',shell=True)
		id__ = int(input('Enter Id(id data bisa di lihat di menu tampilkan data): '))
		tampil_by_id(id__)
		hapus_data(id__)
		input("\n\ndata sudah di hapus \npress enter to back:")
	else:
		return 0;
	return 1;
#perulangan program menu
while(menu()):
	pass