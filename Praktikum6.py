# import tabulate
from tabulate import tabulate

# Midun Hakiki
# TI22B1

datamahasiswa = {
    'No': [],
    'Nim': [],
    'Nama': [],
    'Tugas': [],
    'Uts': [],
    'Uas': [],
    'Nilai Akhir': [],
}
no = 0
# fungsi untuk menampilkan data

def tampilkan():
    print("Berikut data yang ada")
    print(tabulate(datamahasiswa, headers=[ 
            'No', 'Nim', 'Nama', 'Tugas', 'Uts', 'Uas', 'Nilai akhir'], tablefmt="fancy_grid*"))
    
# Fungsi untuk menambahkan data

def tambah(no):
    # menginput data
    nim = int(input("Masukan NIM : "))
    nama = input("Masukan Nama : ")
    tugas = int(input("Masukan Nilai Tugas : "))
    uts = int(input("Masukan Nilai Uts : "))
    uas = int(input("Masukan Nilai Uas : "))
    nilai_akhir  = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
    # menambahkan data
    datamahasiswa['No'].append(no)
    datamahasiswa['No'].append(no)
    datamahasiswa['Nim'].append(nim)
    datamahasiswa['Nama'].append(nama)
    datamahasiswa['Uts'].append(uts)
    datamahasiswa['Tugas'].append(tugas)
    datamahasiswa['Uas'].append(uas)
    datamahasiswa['Nilai Akhir'].append(nilai_akhir)
    print('Data berhasil ditambahkan.')
    # print(tabulate(dataMahasiswa, headers=[
    #       'Nim', 'Nama', 'Tugas', 'Uts', 'Uas', 'Nilai akhir'], tablefmt="fancy_grid*"))
    
# fungsi untuk mengedit data

def ubah(nama):
    # cek jika ada nama tersebut didataMahasiswa
    if nama in datamahasiswa['Nama']:
        # cari posisi indexnya lalu di simpan di nimIndex
        namaIndex = datamahasiswa ['Nama'].index(nama)
        print("Pilih data yang mau diedit")
        # perulangan mengedit data dalam bentuk pilihan
        while True:
            editApa = int(input(
                "(1) Nim, \n (2) Nama, \n (3) Nilai Tugas, \n (4) Nilai Uts, \n (5) Nilai Uas, \n (0) Save perubahan & exit \n :"))
            print("")
            
            if editApa == 1:
                # merubah nim
                newNim = int(input("Masukan Nim :"))
                datamahasiswa['Nim'][namaIndex] = newNim
            elif editApa == 2:
                # merubah nama
                newNama = input("Masukan Nama :")
                datamahasiswa['Nama'][namaIndex] = newNama
            elif editApa == 3:
                # merubah nilai tugas & nilai akhir
                newTugas = int(input("Masukan Nilai Tugas :"))
                nilai_akhir = (newTugas * 30 / 100) + (datamahasiswa['Uts'][namaIndex] * 35 / 100) + (
                    datamahasiswa['Uas'][namaIndex] * 35 / 100)
                datamahasiswa['Tugas'][namaIndex] = newTugas
                datamahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
            elif editApa == 4:
                    # merubah nilai uts & nilai akhir
                newUts = int(input("Masukan Nilai Uts :"))
                nilai_akhir = (datamahasiswa['Tugas'][namaIndex] * 30 / 100) + (newUts * 35 / 100 ) + (
                    datamahasiswa['Uas'][namaIndex] * 35 / 100)
                datamahasiswa['Uts'][namaIndex] = newUts
                datamahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir  
            elif editApa == 5:
                    # merubah nilai uas & nilai akhir
                newUas = int(input("Masukan Nilai Uas :"))
                nilai_akhir = (datamahasiswa['Tugas'][namaIndex] * 30 / 100) + (datamahasiswa['Uts'][namaIndex] * 35 / 100) + (
                    newUas * 35 / 100 )
                datamahasiswa['Uas'][namaIndex] = newUas
                datamahasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
            elif editApa == 0:
                print('Perubahan Data berhasil disimpan,')
                break
    else:
        print("data tidak ditemukan")

#   fungsi untuk menghapus data

def hapus(nama):
    if nama in datamahasiswa['Nama']:
        namaIndex = datamahasiswa['Nama'].index(nama)
        #   menghapus data berdasarkan position index pada nama
        del datamahasiswa['No'][namaIndex]
        del datamahasiswa['Nim'][namaIndex]
        del datamahasiswa['Nama'][namaIndex]
        del datamahasiswa['Tugas'][namaIndex]
        del datamahasiswa['Uts'][namaIndex]
        del datamahasiswa['Uas'][namaIndex]
        del datamahasiswa['Nilai Akhir'][namaIndex]
        print("data berhasil dihapus")
    else:
        print("data tidak ditemukan")

# fungsi untuk mencari data

# melakukan perulangan menggunakan while sampai menekan huruf Q perulangan akan berhenti
while True:
    # opsi input pilihan C,R,U,D,F,Q
    tanya = input(
        "(C) Menambah data,\n (R) Melihat semua data,\n (U) Update data,\n (D) Menghapus data,\n (F) Mencari data,\n (Q) Keluar program :")
    if tanya == "C":
        while True:
            no += 1
            # memangil fungsi tambah data dan memparsing data no
            tambah(no)
            tambahDataLagi = input("Tambah Data Lagi ? (y/n) :")
            if tambahDataLagi == 'n':
                break
    elif tanya == "R":
        # menampilkan data dalam bentuk table mengunakan package tabulate
        tampilkan()
        print("")
    elif tanya == "U":
        print(tabulate(datamahasiswa, headers=[
            'No', 'Nim', 'Nama', 'Tugas', 'Uts', 'Uas', 'Nilai akhir'], tablefmt="fancy_grid"))
        nama = input('Masukan nama yang mau diedit :')
        print("")
        ubah(nama)
    elif tanya == "D":
        print(tabulate(datamahasiswa, headers=[
            'No', 'Nim', 'Nama', 'Tugas', 'Uts', 'Uas', 'Nilai Akhir'], tablefmt="fancy_grid"))
        nama = input('Masukan nama yang mau dihapus :')
        print("")
        hapus(nama)
    elif tanya == "Q":
        print("")
        print("Anda telah keluar dari program.")
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    