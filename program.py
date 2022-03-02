def pertama():
    print('Selamat Datang di Safik Hidayahs Train\n')

    def welcome() :
          awal=input('Apakah anda ingin melakukan pemesanan tiket(ya/tidak):')
          if awal=='ya' :
            print('Selamat Datang di Menu Pemesanan Tiket')
          elif awal=='tidak' :
            quit()
                     
          else:
            print('input salah')
            welcome()
    welcome()

    nama= input('Silahkan masukkan nama: ')
    print('Nama: ' ,nama)
    nomor= int(input('Silahkan masukkan nomor HP: '))
    print('Nomor HP: ' ,nomor)



    print('Rute Kerete SnowPiercer')
    Rutekereta= ['1.Jakarta - Bandung', '2.Jakarta - Surabaya\n']
    for menu1 in Rutekereta :
        print(menu1, end=' \n')

    def rute () :
        menukelas=int(input('Silahkan masukan opsi perjalanan (angka) :'))
        if menukelas== 1:
            print('berhasil memilih rute perjalanan Jakarta - Bandung berhasil')
        elif menukelas== 2:
            print('berhasil memilih rute perjalanan Jakarta - Surabaya berhasil')
        else:
            print('input salah ')
            print('silahkan masukan nomor kemabali')
            rute()
    rute()

    print('Kelas Perjalanan ')
    menuPemesanan= ['1.VIP','2.Bisnis', '3.Ekonomi', '4.Regular\n']
    for menu2 in menuPemesanan:
        print (menu2, end=' ')
        
        
    def kelas() :
        menukelas=int (input ('Silahkan Memasukan Angka berdasarkan tiket kelas yang tersedia: '))
        if menukelas== 1:
            print('Berhasil Memesan VIP Class')
        elif menukelas== 2:
            print('Berhasil Memesan Bisnis Class')
        elif menukelas== 3 :
            print('Berhasil Memesan Ekonomi Class')
        elif menukelas== 4 :
            print('Berhasil Memesan Regular Class')
        else:
            print('input salah')
            print('silahkan masukan nomor kemabali')
            kelas ()
    kelas ()

    print('Metode Pembayaran Tiket ')
    metodepembayaran= ['1. Tunai, 2. Non Tunai\n']
    for menu3 in metodepembayaran:
        print(menu3, end=' ')
                               
    def metode() :
        metodebayar= int(input('Silahkan Memasukan Angka metode pembayaran: '))
        if metodebayar== 1 :
            print('Terima kasih telah melakukan pembelian tiket')
            print('Tolong ambil struk, dan lakukan pembayaran di Loket')
            exit()
        elif metodebayar== 2 :
            print('Silahkan menyelesaikan pembayaran')
        else:
            print('input salah')
            print('silahkan masukan nomor kemabali')
            metode()

        uang=int(input('Silahkan memasukan uang sebesar Rp.500.000,00 :'))
        if uang>= 10000:
            hasil=uang-5000000
            print ('Kembalian uang anda', hasil)
            print ('Pembayaran selesai, menampilkan tiket online', nama, ' ', nomor)
        elif uang< 300000:
            print('uang Anda tidak mencukupi')
        metode()

    metode()

    def last() :
        again=(input('Apakah anda ingin melakukan pembelian lagi (y/n) :'))
        if again=='y' :
            pertama()
        elif again=='n' :
            print('Terima kasih telah melakukan pembelian tiket di Safik Hidayahs Train')
            quit()
        else:
            print('input salah')
            last()
    last()
pertama()