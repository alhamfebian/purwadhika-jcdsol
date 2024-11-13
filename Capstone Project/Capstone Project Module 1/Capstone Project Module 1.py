# Capstone Project Module 1: Data Karyawan Perusahaan

print('\nSelamat Datang Di Sistem Data Karayawan Perusahaan PT. Selalu Pusing :)\n')
print('Silahkan Pilih Sistem Yang Ingin Anda Jalankan\n')

# Global Variable
dataKaryawan = {
    # 000X adalah ID Setiap Karyawan (Unique)
    # jenisKelamin: L = Laki-Laki, P = Perempuan
    '0001': {
        'namaLengkap': 'Andi Pratama',
        'jenisKelamin': 'L',
        'divisi': 'Pemasaran'
    },
    '0002': {
        'namaLengkap': 'Siti Aisyah',
        'jenisKelamin': 'P',
        'divisi': 'Produk'
    },
    '0003': {
        'namaLengkap': 'Budi Santoso',
        'jenisKelamin': 'L',
        'divisi': 'Keuangan'
    },
    '0004': {
        'namaLengkap': 'Dian Sari',
        'jenisKelamin': 'P',
        'divisi': 'Penjualan'
    },
    '0005': {
        'namaLengkap': 'Rudi Setiawan',
        'jenisKelamin': 'L',
        'divisi': 'Operasional'
    }
}

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


def menampilkanSemuaDataKaryawan():
    print("|ID   | Nama Lengkap\t| Jenis Kelamin | Divisi\t|\n")
    for key, item in dataKaryawan.items():
        print(f"|{key} | {item['namaLengkap']}\t| {item['jenisKelamin']}\t\t| {item['divisi']}\t|")


userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5): \n'))

while userInput != 5:
    if (userInput == 1):
        menampilkanSemuaDataKaryawan()

        userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5): '))
    else:
        print('Terima Kasih, Sampai Bertemu Di Lain Waktu! :)')
        break