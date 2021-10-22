usd = float(14131.1)
sgd = float(10517.71)
eur = float(16456.39)
jpy = float(123.69)
hi = ("NOMINAL UANG ")
ke = (" ANDA: ")
dalam = ("NOMINAL UANG ANDA SETELAH DI KONVERSIKAN ADALAH ")
nama = (" RUPIAH"," DOLLAR AMERIKA"," DOLLAR SINGAPURA"," EURO"," YEN")
salah = ("FORMAT YANG ANDA MASUKKAN SALAH")

while (True):
    print ("KONVERSI MATA UANG\n","1. IDR\n","2. USD\n","3. SGD\n","4. EUR\n","5. JPY\n")
    awal = input ("APA MATA UANG AWAL ANDA? ")
    akhir = input ("MAU DI KONVERSIKAN KEMANA? ")


    print ("\n")

    if awal == "1":
        frt = input (f"{hi}\b{nama[0]}{ke}")
        if frt < "a" :
            print ()
        else :
            akhir = 0
    elif awal == "2":
        kop = input (f"{hi}\b{nama[1]}{ke}")
        if kop < "a" :
            frt = float(kop)*usd
        else :
            akhir = 0
    elif awal == "3":
        kop = input (f"{hi}\b{nama[2]}{ke}")
        if kop <"a" :
            frt = float(kop)*sgd
        else :
            akhir = 0
    elif awal == "4":
        kop = input (f"{hi}\b{nama[3]}{ke}")
        if kop <"a" :
             frt = float(kop)*eur
        else :
            akhir = 0
    elif awal == "5":
        kop = input (f"{hi}\b{nama[4]}{ke}")
        if kop <"a" :
            frt = float(kop)*jpy
        else :
            akhir = 0
    else :
        akhir = 0

    if akhir == "1":
        nilai = float(frt) / 1
        kl = nama[0]
        break
    if akhir == "2":
        nilai = float(frt)/float(usd)
        kl = nama[1]
        break
    if akhir == "3":
        nilai = float(frt)/float(sgd)
        kl = nama[2]
        break
    if akhir == "4":
        nilai = float(frt)/float(eur)
        kl = nama[3]
        break
    if akhir == "5":
        nilai = float(frt)/float(jpy)
        kl = nama [4]
        break
    else :
        print (f"\n{salah}\n")
ex = round(nilai, 2)
ribuan = f"{ex:,}"
print (f"{dalam}{ribuan}{kl}")
if ex == 0.0:
    print("\nitu duit atau harga diriku dimatamu sih? kok ga ada harganya banget\n")
