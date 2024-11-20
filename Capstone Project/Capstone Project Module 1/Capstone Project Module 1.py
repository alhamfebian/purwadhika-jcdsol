# Capstone Project Module 1: Data Karyawan Perusahaan

print('\nSelamat Datang Di Sistem Data Karayawan Perusahaan PT. Selalu Pusing :)\n')
print('Silahkan Pilih Sistem Yang Ingin Anda Jalankan\n')

# Kumpulan Global Variable

# jenisKelamin: L = Laki-Laki, P = Perempuan
dataPerusahaan = {
    'Teknologi': {
        'Andi Pratama': {
            'Jenis Kelamin': 'L',
            'Gaji': 10000000
        },
        'Siti Aisyah': {
            'Jenis Kelamin': 'P',
            'Gaji': 20000000
        }
    },
    'Pemasaran': {
        'Budi Santoso': {
            'Jenis Kelamin': 'L',
            'Gaji': 25000000
        },
        'Dian Sari': {
            'Jenis Kelamin': 'P',
            'Gaji': 15000000
        },
    },
    'Penjualan': {
        'Rudi Setiawan': {
            'Jenis Kelamin': 'L',
            'Gaji': 15000000
        },
        'Rani Putri': {
            'Jenis Kelamin': 'P',
            'Gaji': 12000000
        }
    }
}

isLoopingEligible = True

# Fungsi untuk print menu system yang bisa dipilih
def printListOfSystemMenu() :
    listOfSystemMenu = [
        '\n1. Menampilkan Semua Data Karyawan PT. Selalu Pusing',
        '2. Menambah Data Karyawan Baru',
        '3. Menghapus Data Karyawan',
        '4. Ubah Data Karyawan',
        '5. Pindah Karyawan Ke Divisi Lain',
        '6. Recap Total Karyawan PT. Selalu Pusing',
        '7. Recap Total Karyawan Per Divisi PT. Selalu Pusing',
        '8. Rata-Rata Gaji Per Divisi PT. Selalu Pusing Per Bulan',
        '9. Rata-Rata Gaji PT. Selalu Pusing',
        '99. Keluar Dari Sistem Data Karayawan Perusahaan PT. Selalu Pusing'
    ]
    for item in listOfSystemMenu:
        print(item)


# Fungsi untuk menampilkan semua data karyawan PT. Selalu Pusing (Menu Sistem Nomor 1)
def menampilkanSemuaDataKaryawan():
    print("| Nama Lengkap\t| Jenis Kelamin | Gaji\t\t| Divisi    |\n")
    for firstKey, value in dataPerusahaan.items():
        for secondKey, item in value.items():
            print(f"| {secondKey}\t| {item['Jenis Kelamin']}\t\t| Rp{item['Gaji']:,.0f}\t| {firstKey} |")
        

# Fungsi untuk menambah data karyawan baru (Menu Sistem Nomor 2)
def menambahKaryawanBaru(divisiKaryawanBaru, namaLengkapKaryawanBaru, jenisKelaminKaryawanBaru, gajiKaryawanBaru):
    tempNamaKaryawan = namaLengkapKaryawanBaru

    # Untuk validasi apakah nama karyawan sudah atau belum di divisi tersebut
    while tempNamaKaryawan in dataPerusahaan[divisiKaryawanBaru]:
        tempNamaKaryawan = input('Nama Karyawan Sudah Ada, Silahkan Masukan Nama Karyawan Yang Lain: ')
    
    dataPerusahaan[divisiKaryawanBaru][tempNamaKaryawan] = {
        'Jenis Kelamin': jenisKelaminKaryawanBaru,
        'Gaji': gajiKaryawanBaru
    }

    print(f'\nKaryawan {namaLengkapKaryawanBaru} berhasil ditambahkan di divisi {divisiKaryawanBaru}! Untuk melihat lebih detail, silahkan pilih menu nomor 1')

    
# Fungsi untuk menghapus data karyawan PT. Selalu Pusing (Menu Sistem Nomor 3)
def menghapusKaryawanBerdasarkanNama(divisiYangDipilihUser, karyawanYangDipilihUser, listKaryawan):
    while karyawanYangDipilihUser not in listKaryawan:
        karyawanYangDipilihUser = input('Nama Karyawan Tidak Ada, Input Nama Karyawan Yang Benar: ')

    del dataPerusahaan[divisiYangDipilihUser][karyawanYangDipilihUser]

    print(f'\nData Karyawan {karyawanYangDipilihUser} berhasil dihapus dari divisi {divisiYangDipilihUser}! Untuk melihat lebih detail, silahkan pilih menu nomor 1')

# Fungsi untuk update data karyawan PT. Selalu Pusing (Menu Sistem Nomor 4)
# Untuk saat ini, scope data yang bisa diubah Jenis Kelamin dan Gaji
def updateDataKaryawan(divisiYangDipilihUser, karyawanYangDipilihUser, fieldYangInginDiubah, valueUntukFieldBaru):
    dataPerusahaan[divisiYangDipilihUser][karyawanYangDipilihUser][fieldYangInginDiubah] = valueUntukFieldBaru

    print(f'\nData {fieldYangInginDiubah} untuk Karyawan {karyawanYangDipilihUser} berhasil diubah! Untuk melihat lebih detail, silahkan pilih menu nomor 1')


# Fungsi untuk memindahkan karyawan ke divisi lain PT. Selalu Pusing (Menu Sistem Nomor 5)
def memindahkanKaryawanKeDivisiLain(divisiKaryawanYangLama, namaKaryawanYangInginDipindah, divisiKaryawanBaru):
    dataPerusahaan[divisiKaryawanBaru][namaKaryawanYangInginDipindah] = {
        'Jenis Kelamin': dataPerusahaan[divisiKaryawanYangLama][namaKaryawanYangInginDipindah]['Jenis Kelamin'],
        'Gaji': dataPerusahaan[divisiKaryawanYangLama][namaKaryawanYangInginDipindah]['Gaji']
    }

    del dataPerusahaan[divisiKaryawanYangLama][namaKaryawanYangInginDipindah]

    print(f'\nKaryawan {namaKaryawanYangInginDipindah} berhasil dipindahkan dari divisi {divisiKaryawanYangLama} ke divisi {divisiKaryawanBaru}! Untuk melihat lebih detail, silahkan pilih menu nomor 1')
    

# Fungsi ini untuk mengetahui berapa jumlah total karyawan PT. Selalu Pusing (Menu Sistem Nomor 6)
def recapTotalJumlahKaryawan():
    totalJumlahKaryawan = 0

    for key, value in dataPerusahaan.items():
        totalJumlahKaryawan += len(dataPerusahaan[key])
    
    print(f'\nTotal Karyawan PT. Selalu Pusing adalah: {totalJumlahKaryawan}')


# Fungsi ini untuk mengetahui berapa jumlah total karyawan PT. Selalu Pusing Per Divisi (Menu Sistem Nomor 7)
def recapTotalJumlahKaryawanPerDivisi():
    for key, value in dataPerusahaan.items():
        print(f'\nDivisi: {key} memiliki: {len(dataPerusahaan[key])} karyawan\n')


# Fungsi untuk mengetahui gaji karyawan Per Divisi PT. Selalu Pusing Per Bulan (Menu Sistem Nomor 8)
def rataRataGajiKaryawanPerDivisi():
    totalGajiKaryawanPerDivisi = 0
    totalRataRataGajiPerDivisi = 0

    for firstKey, value in dataPerusahaan.items():
        for secondKey, item in value.items():
            totalGajiKaryawanPerDivisi += dataPerusahaan[firstKey][secondKey]['Gaji']

        totalRataRataGajiPerDivisi = totalGajiKaryawanPerDivisi / len(dataPerusahaan[firstKey])
        print(f'Total Gaji Divisi {firstKey} adalah: Rp{totalGajiKaryawanPerDivisi:,.0f} dengan jumlah karyawan di divisi {firstKey} adalah: {len(dataPerusahaan[firstKey])}')
        print(f'Rata-Rata Gaji Divisi {firstKey} Per Bulan adalah: Rp{totalRataRataGajiPerDivisi:,.0f}\n')

        # Untuk me-reset perhitungan total dan rata-rata gaji karyawan per divisi
        totalRataRataGajiPerDivisi = 0
        totalGajiKaryawanPerDivisi = 0


# Fungsi untuk mengetahui gaji karyawan PT. Selalu Pusing Per Bulan (Menu Sistem Nomor 9)
def rataRataGajiPerusahaan():
    totalGajiKaryawan = 0
    totalKaryawan = 0
    totalRataRataGajiKaryawan = 0

    for firstKey, value in dataPerusahaan.items():
        for secondKey, item in value.items():
            totalGajiKaryawan += dataPerusahaan[firstKey][secondKey]['Gaji']
        totalKaryawan += len(dataPerusahaan[firstKey])

    totalRataRataGajiKaryawan = totalGajiKaryawan / totalKaryawan

    print(f'\nTotal Gaji Karyawan PT.Selalu Pusing adalah: Rp{totalGajiKaryawan:,.0f}')
    print(f'\nTotal Karyawan PT.Selalu Pusing adalah: {totalKaryawan} karyawan')
    print(f'\nRata-Rata Gaji Karyawan PT.Selalu Pusing adalah: Rp{totalRataRataGajiKaryawan:,.0f}')


# Fungsi untuk validasi input user untuk field 'Jenis Kelamin'
def validasiJenisKelamin(dataJenisKelamin):
    tempJenisKelaminKaryawanBaru = dataJenisKelamin
        
    # Looping ini untuk memvalidasi input user, user hanya bisa input L / P
    while tempJenisKelaminKaryawanBaru != 'L' and tempJenisKelaminKaryawanBaru != 'P':
        tempJenisKelaminKaryawanBaru = input('Input untuk Jenis Kelamin tidak valid, Masukan Input yang valid L / P: ')

    return tempJenisKelaminKaryawanBaru
    

# Menampilkan menu dan menerima input pertama kali dari user
printListOfSystemMenu()
try:
    userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
except:
    print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
    userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))

while isLoopingEligible:

    # Jika user memilih menu untuk menampilkan seluruh data karyawan
    if (userInput == 1):
        menampilkanSemuaDataKaryawan()

        # Menampilkan menu untuk memudahkan user memilih menu yang ingin dijalankan
        printListOfSystemMenu()
        try:
            userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
        except:
            print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
            userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
    ##################################################################### END OF USER INPUT = 1 ###########################################################


    # Jika user memilih menu untuk menambah karyawan baru 
    elif (userInput == 2):
        userInginMenlanjutkanPilihan = input('\nApakah Anda Ingin Menambahkan Data Karyawan Baru? Input Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        while userInginMenlanjutkanPilihan != 'Y' and userInginMenlanjutkanPilihan != 'T':
            userInginMenlanjutkanPilihan = input('Masukan Input Yang Benar, Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        if userInginMenlanjutkanPilihan == 'T':
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
        
        else:
            listDivisi = list(dataPerusahaan.keys())

            for divisi in listDivisi:
                print(divisi)

            divisiYangDipilihUser = input('Pilih Divisi Untuk Karyawan Baru: ')

            while divisiYangDipilihUser not in listDivisi: 
                divisiYangDipilihUser = input('Nama Divisi Yang Dipilih Tidak Ada, Masukan Divisi Yang Benar: ')

            namaLengkapKaryawanBaru = input('Masukan Nama Karyawan Baru: ')
            jenisKelaminKaryawanBaru = input('Masukan Jenis Kelamin Karyawan Baru (L/P): ')
            
            try:
                gajiKaryawanBaru = int(input('Masukan Gaji Karyawan Baru: '))
            except:
                gajiKaryawanBaru = int(input('Value Gaji harus tipe data Integer, Silahkan masukan yang benar (eg. 1000000): '))

            jenisKelaminKaryawanBaru = validasiJenisKelamin(jenisKelaminKaryawanBaru)

            menambahKaryawanBaru(divisiYangDipilihUser, namaLengkapKaryawanBaru, jenisKelaminKaryawanBaru, gajiKaryawanBaru)

            # Menampilkan menu untuk memudahkan user memilih menu yang ingin dijalankan
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
    ##################################################################### END OF USER INPUT = 2 ##############################################################


    # Jika user memilih menu untuk menghapus data karyawan 
    elif (userInput == 3):
        userInginMenlanjutkanPilihan = input('\nApakah Anda Ingin Menghapus Data Karyawan? Input Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        while userInginMenlanjutkanPilihan != 'Y' and userInginMenlanjutkanPilihan != 'T':
            userInginMenlanjutkanPilihan = input('Masukan Input Yang Benar, Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        if userInginMenlanjutkanPilihan == 'T':
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
        
        else:
            print('\nBerikut Adalah Divisi Yang Ada Di PT. Selalu Pusing')
            listDivisi = list(dataPerusahaan.keys())

            for divisi in listDivisi:
                print(divisi)

            divisiYangDipilihUser = input('Pilih Divisi Karyawan Yang Ingin Di Hapus: ')

            while divisiYangDipilihUser not in listDivisi:
                divisiYangDipilihUser = input('Nama Divisi Yang Dipilih Tidak Ada, Masukan Divisi Yang Benar: ')

            print(f'\nBerikut Adalah Nama-Nama Karyawan Yang Ada Di Divisi {divisiYangDipilihUser} PT. Selalu Pusing\n')
            listKaryawan = list(dataPerusahaan[divisiYangDipilihUser].keys())

            for karyawan in listKaryawan:
                print(karyawan)

            karyawanYangDipilihUser = input(f'Pilih Nama Karyawan Yang Ingin Di Hapus Dari Divisi {divisiYangDipilihUser}: ')
        
            menghapusKaryawanBerdasarkanNama(divisiYangDipilihUser, karyawanYangDipilihUser, listKaryawan)

            # Menampilkan menu untuk memudahkan user memilih menu yang ingin dijalankan
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
    ##################################################################### END OF USER INPUT = 3 ##############################################################


    # Jika user memilih menu untuk meng-update data karyawan 
    elif (userInput == 4):
        userInginMenlanjutkanPilihan = input('\nApakah Anda Ingin Mengubah Data Karyawan? Input Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        while userInginMenlanjutkanPilihan != 'Y' and userInginMenlanjutkanPilihan != 'T':
            userInginMenlanjutkanPilihan = input('Masukan Input Yang Benar, Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        if userInginMenlanjutkanPilihan == 'T':
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))

        else:
            print('\nBerikut Adalah Divisi Yang Ada Di PT. Selalu Pusing\n')
            listDivisi = list(dataPerusahaan.keys())

            for divisi in listDivisi:
                print(divisi)

            
            divisiYangDipilihUser = input('Pilih Divisi Karyawan Yang Ingin Diubah: ')

            while divisiYangDipilihUser not in listDivisi:
                divisiYangDipilihUser = input('Nama Divisi Yang Dipilih Tidak Ada, Masukan Divisi Yang Benar: ')

            print(f'\nBerikut Adalah Nama-Nama Karyawan Yang Ada Di Divisi {divisiYangDipilihUser} PT. Selalu Pusing\n')
            listKaryawan = list(dataPerusahaan[divisiYangDipilihUser].keys())

            for karyawan in listKaryawan:
                print(karyawan)
           
            karyawanYangDipilihUser = input('Pilih Nama Karyawan Yang Ingin Diubah Datanya: ')

            while karyawanYangDipilihUser not in listKaryawan:
                karyawanYangDipilihUser = input('Nama Karyawan Tidak Ada, Input Nama Karyawan Yang Benar: ')

            print('\nBerikut Adalah Field Yang Bisa Di Ubah\n')
            tempListFieldKaryawan = []

            # Looping ini hanya untuk mengambil Field-Field yang dimiliki karyawan
            for firstKey, value in dataPerusahaan.items():
                for secondKey, item in value.items():
                    tempListFieldKaryawan.append(dataPerusahaan[firstKey][secondKey].keys())


            # [0] untuk mengambil 2 field utama, karena sisanya valuenya sama saja (Jenis Kelamin dan Gaji)
            listFieldKaryawan = list(tempListFieldKaryawan[0])

            for item in listFieldKaryawan:
                print(item)

            fieldYangInginDiubah = input('Pilih Field Yang Ingin Diubah: ')

            while fieldYangInginDiubah not in listFieldKaryawan:
                fieldYangInginDiubah = input('Field Yang Dipilih Tidak Ada, Masukan Field Yang Benar (Jenis Kelamin, Gaji): ')
        
            valueUntukFieldBaru = ''

            if fieldYangInginDiubah == 'Jenis Kelamin':
                valueUntukFieldBaru = validasiJenisKelamin(input('Masukan Value Baru Untuk Jenis Kelamin (L/P): '))
            else:
                try:
                    valueUntukFieldBaru = int(input('Masukan Value Baru Untuk Gaji: '))
                except:
                    valueUntukFieldBaru = int(input('Value Gaji harus tipe data Integer, Silahkan masukan yang benar (eg. 1000000): '))

            updateDataKaryawan(divisiYangDipilihUser, karyawanYangDipilihUser, fieldYangInginDiubah, valueUntukFieldBaru)

            # Menampilkan menu untuk memudahkan user memilih menu yang ingin dijalankan
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
    ##################################################################### END OF USER INPUT = 4 #############################################################


    # Jika user memilih menu untuk memindahkan karyawan ke divisi lain
    elif (userInput == 5):
        userInginMenlanjutkanPilihan = input('\nApakah Anda Ingin Memindah Karyawan Ke Divisi Lain? Input Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        while userInginMenlanjutkanPilihan != 'Y' and userInginMenlanjutkanPilihan != 'T':
            userInginMenlanjutkanPilihan = input('Masukan Input Yang Benar, Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        if userInginMenlanjutkanPilihan == 'T':
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))

        else:
            menampilkanSemuaDataKaryawan()

            listDivisi = list(dataPerusahaan.keys())

            for divisi in listDivisi:
                print(divisi)

            divisiKaryawanLama = input('Pilih Divisi Lama Karyawan Yang Ingin Dipindah: ')

            while divisiKaryawanLama not in listDivisi:
                divisiKaryawanLama = input('Nama Divisi Yang Dipilih Tidak Ada, Masukan Divisi Yang Benar: ')


            while len(dataPerusahaan[divisiKaryawanLama]) == 0:
                divisiKaryawanLama = input(f'Divisi {divisiKaryawanLama} Tidak Memiliki Karyawan, Silahkan Pilih Divisi Yang Lain: ')

            print(f'\nBerikut Adalah Nama Karyawan-Karyawan divisi {divisiKaryawanLama}: ')
            listKaryawan = list(dataPerusahaan[divisiKaryawanLama].keys())

            for karyawan in listKaryawan:
                print(karyawan)

            karyawanYangInginDipindah = input('Pilih Nama Karyawan Yang Ingin Dipindah: ')

            while karyawanYangInginDipindah not in listKaryawan:
                karyawanYangInginDipindah = input('Nama Karyawan Tidak Ada, Input Nama Karyawan Yang Benar: ')

            print('\nSilahkan Pilih Divisi Untuk Karyawan Yang Ingin Dipindah: ')
            listDivisi = list(dataPerusahaan.keys())

            for divisi in listDivisi:
                print(divisi)

            divisiBaruKaryawan = input('Pilih Divisi Baru Untuk Karyawan: ')

            while divisiBaruKaryawan not in listDivisi:
                divisiBaruKaryawan = input('Nama Divisi Yang Dipilih Tidak Ada, Masukan Divisi Yang Benar: ')

            memindahkanKaryawanKeDivisiLain(divisiKaryawanLama, karyawanYangInginDipindah, divisiBaruKaryawan)

            # Menampilkan menu untuk memudahkan user memilih menu yang ingin dijalankan
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
    ##################################################################### END OF USER INPUT = 5 ##############################################################
    

    # Jika user memilih menu untuk melihat recap total karyawan PT.Selalu Pusing 
    elif (userInput == 6):
        userInginMenlanjutkanPilihan = input('\nApakah Anda Ingin Melihat Recap Total Karyawan PT.Selalu Pusing? Input Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        while userInginMenlanjutkanPilihan != 'Y' and userInginMenlanjutkanPilihan != 'T':
            userInginMenlanjutkanPilihan = input('Masukan Input Yang Benar, Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        if userInginMenlanjutkanPilihan == 'T':
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))

        else:
            recapTotalJumlahKaryawan()
            
            # Menampilkan menu untuk memudahkan user memilih menu yang ingin dijalankan
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
    ##################################################################### END OF USER INPUT = 6 ##############################################################


    # Jika user memilih menu untuk melihat recap total karyawan PT.Selalu Pusing Per divisi
    elif (userInput == 7):
        userInginMenlanjutkanPilihan = input('\nApakah Anda Ingin Melihat Recap Total Karyawan Per Divisi PT.Selalu Pusing? Input Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        while userInginMenlanjutkanPilihan != 'Y' and userInginMenlanjutkanPilihan != 'T':
            userInginMenlanjutkanPilihan = input('Masukan Input Yang Benar, Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        if userInginMenlanjutkanPilihan == 'T':
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))

        else:
            recapTotalJumlahKaryawanPerDivisi()

            # Menampilkan menu untuk memudahkan user memilih menu yang ingin dijalankan
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
    ##################################################################### END OF USER INPUT = 7 #############################################################


    # Jika user memilih menu untuk melihat recap total gaji karyawan PT.Selalu Pusing per divisi per bulan
    elif (userInput == 8):
        userInginMenlanjutkanPilihan = input('\nApakah Anda Ingin Melihat Rata-Rata Gaji Per Divisi PT.Selalu Pusing Per Bulan? Input Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        while userInginMenlanjutkanPilihan != 'Y' and userInginMenlanjutkanPilihan != 'T':
            userInginMenlanjutkanPilihan = input('Masukan Input Yang Benar, Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        if userInginMenlanjutkanPilihan == 'T':
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))

        else:
            rataRataGajiKaryawanPerDivisi()

            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
    ##################################################################### END OF USER INPUT = 8 #############################################################


    # Jika user memilih menu untuk mengetahui rata-rata gaji PT.Selalu Pusing 
    elif (userInput == 9):
        userInginMenlanjutkanPilihan = input('\nApakah Anda Ingin Melihat Rata-Rata Gaji PT.Selalu Pusing? Input Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        while userInginMenlanjutkanPilihan != 'Y' and userInginMenlanjutkanPilihan != 'T':
            userInginMenlanjutkanPilihan = input('Masukan Input Yang Benar, Y untuk melanjutkan, T untuk kembali ke menu utama: ')

        if userInginMenlanjutkanPilihan == 'T':
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
        else:
            rataRataGajiPerusahaan()

            # Menampilkan menu untuk memudahkan user memilih menu yang ingin dijalankan
            printListOfSystemMenu()
            try:
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
            except:
                print('Input Harus Dalam Bentuk Angka (eg. 1,2,3,4,5,6,7,8,9,99)')
                userInput = int(input('\nMasukan Angka Menu Yang Ingin Anda Jalankan (eg. 1,2,3,4,5,6,7,8,9) atau Masukan Angka 99 untuk mengakhiri sistem: '))
    ##################################################################### END OF USER INPUT = 9 ##############################################################


    # Jika user memilin menu untuk mengakhiri sistem
    elif (userInput == 99):
        print('Terima Kasih, Sampai Bertemu Di Lain Waktu! :)')
        isLoopingEligible = False
    ################# END OF USER INPUT = 99 ###################

    else:
        print('Terima Kasih, Sampai Bertemu Di Lain Waktu! :)')
        isLoopingEligible = False