# Capstone Project Module 1: Data Karyawan Perusahaan

print('\nSelamat Datang Di Sistem Data Karayawan Perusahaan PT. Selalu Pusing :)\n')
print('Silahkan Pilih Sistem Yang Ingin Anda Jalankan\n')

# Global Variable
dataKaryawan = {

    # jenisKelamin: L = Laki-Laki, P = Perempuan
    'Andi Pratama': {
        'Jenis Kelamin': 'L',
        'Divisi': 'Pemasaran'
    },
    'Siti Aisyah': {
        'Jenis Kelamin': 'P',
        'Divisi': 'Produk'
    },
    'Budi Santoso': {
        'Jenis Kelamin': 'L',
        'Divisi': 'Keuangan'
    },
    'Dian Sari': {
        'Jenis Kelamin': 'P',
        'Divisi': 'Penjualan'
    },
    'Rudi Setiawan': {
        'Jenis Kelamin': 'L',
        'Divisi': 'Operasional'
    }
}

# Fungsi untuk print menu system yang bisa dipilih
def printListOfSystemMenu() :
    listOfSystemMenu = [
        '1. Menampilkan Semua Data Karyawan PT. Selalu Pusing',
        '2. Menambah Data Karyawan Baru',
        '3. Menghapus Data Karyawan',
        '4. Update Data Karyawan',
        '5. Keluar Dari Sistem Data Karayawan Perusahaan PT. Selalu Pusing'
    ]
    for item in listOfSystemMenu:
        print(item)

printListOfSystemMenu()

# Fungsi untuk menampilkan semua data karyawan PT. Selalu Pusing (Menu Sistem Nomor 1)
def menampilkanSemuaDataKaryawan():
    print("|Nama Lengkap\t| Jenis Kelamin | Divisi\t|\n")
    for key, item in dataKaryawan.items():
        print(f"|{key} | {item['Jenis Kelamin']}\t\t| {item['Divisi']}\t|")

# Fungsi untuk menambah data karyawan baru (Menu Sistem Nomor 2)
def menambahKaryawanBaru(namaLengkapKaryawanBaru = 'Asep', jenisKelaminKaryawanBaru = 'L', divisiKaryawanBaru = 'Teknologi'):

    if (namaLengkapKaryawanBaru in dataKaryawan):
        print('Nama Karyawan Sudah Ada, Silahkan Masukan Nama Karyawan Yang Lain')
        tempNamaKaryawan = input('Masukin Nama Karyawan Baru: ')
        dataKaryawan[tempNamaKaryawan] = {
            'Jenis Kelamin': jenisKelaminKaryawanBaru,
            'Divisi': divisiKaryawanBaru
        }
    
    else:
        dataKaryawan[namaLengkapKaryawanBaru] = {
            'Jenis Kelamin': jenisKelaminKaryawanBaru,
            'Divisi': divisiKaryawanBaru
        }

    

# Fungsi untuk menghapus data karyawan PT. Selalu Pusing (Menu Sistem Nomor 3)
def menghapusKaryawanBerdasarkanNama(namaKaryawanYangAkanDiHapus):
    
    if (namaKaryawanYangAkanDiHapus in dataKaryawan):
        del dataKaryawan[namaKaryawanYangAkanDiHapus]
    else:
        print('Nama Karyawan Tidak Ada, Silahkan Masukan Kembali Nama Karyawan Yang Benar')
        namaKaryawanYangAkanDiHapus = input('Pilih Nama Karyawan Yang Ingin Di Hapus: ')
        del dataKaryawan[namaKaryawanYangAkanDiHapus]

# Fungsi untuk update data karyawan PT. Selalu Pusing menggunakan ID sebagai primary key (Menu Sistem Nomor 4)
# Data yang bisa diupdate hanya jenis kelamin dan divisi, Nama tidak bisa diupdate karena merupakan primary key
def updateDataKaryawan(namaKaryawanYangAkanDiubah, dataYangInginDiubah, valueDataYangBaru):

    if (namaKaryawanYangAkanDiubah in dataKaryawan):
        dataKaryawan[namaKaryawanYangAkanDiubah][dataYangInginDiubah] = valueDataYangBaru
    else:
        print('Nama Karyawan Tidak Ada, Silahkan Masukan Kembali Nama Karyawan Yang Benar')
        namaKaryawanYangAkanDiubah = input('Pilih Nama Karyawan Yang Ingin Di Update: ')
        dataKaryawan[namaKaryawanYangAkanDiubah][dataYangInginDiubah] = valueDataYangBaru

# Fungsi untuk recap data karyawan PT. Selalu Pusing berdasarkan Divis (Menu Sistem Nomor 5)
# Fungsi ini untuk mengetahui berapa jumlah total karyawan PT. Selalu Pusing
def recapDataKaryawan():
    print(f'Total Karyawan PT. Selalu Pusing adalah: {len(dataKaryawan)}')


try:
    userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5): '))
except:
    print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5)')
    userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5): '))

while userInput != 6:
    if (userInput == 1):
        menampilkanSemuaDataKaryawan()

        userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5): '))
    elif (userInput == 2):
        namaLengkapKaryawanBaru = input('Masukan Nama Karyawan Baru: ')
        jenisKelaminKaryawanBaru = input('Masukan Jenis Kelamin Karyawan Baru (L/P): ')
        divisiKaryawanBaru = input('Masukan Divisi Karyawan Baru: ')

        menambahKaryawanBaru(namaLengkapKaryawanBaru, jenisKelaminKaryawanBaru, divisiKaryawanBaru)

        userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5): '))

    elif (userInput == 3):
        kumpulanNamaKaryawan = list(dataKaryawan.keys())
        print('Berikut Adalah Nama-Nama Karyawan Yang Ada Di PT. Selalu Pusing')
        
        for item in kumpulanNamaKaryawan:
            print(item)
        
        namaKaryawanYangAkanDiHapus = input('Pilih Nama Karyawan Yang Ingin Di Hapus: ')

        menghapusKaryawanBerdasarkanNama(namaKaryawanYangAkanDiHapus)

        userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5): '))

    elif (userInput == 4):
        
        kumpulanKaryawan = list(dataKaryawan.keys())
        kumpulanFieldDataKaryawan = []

        for firstKey, value in dataKaryawan.items():
            for secondKey, item in value.items():
                kumpulanFieldDataKaryawan.append(secondKey)

        print('Berikut Adalah Nama-Nama Karyawan Yang Ada Di PT. Selalu Pusing')

        for item in kumpulanKaryawan:
            print(item)
        
        namaKaryawanYangAkanDiubah = input('Pilih Nama Karyawan Yang Ingin Di Update: ')

        for item in kumpulanFieldDataKaryawan[0:2]:
            print(item)

        dataYangInginDiubah = input('Pilih Field Yang Ingin Di Update: ')
        valueDataYangBaru = input('Masukan Data Baru: ')


        updateDataKaryawan(namaKaryawanYangAkanDiubah, dataYangInginDiubah, valueDataYangBaru)

        userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5): '))
    elif (userInput == 5):
        recapDataKaryawan()

        userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5): '))
    else:
        print('Terima Kasih, Sampai Bertemu Di Lain Waktu! :)')
        break