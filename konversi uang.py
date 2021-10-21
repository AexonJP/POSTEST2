usd = float(14131.1)
sgd = float(10517.71)
eur = float(16456.39)
jpy = float(123.69)
hi = ("NOMINAL UANG ")
ke = (" ANDA: ")
dalam = ("NOMINAL UANG ANDA SETELAH DI KONVERSIKAN ADALAH ")
nama = (" RUPIAH"," DOLLAR AMERIKA"," DOLLAR SINGAPURA"," EURO"," YEN")

while (True):
    print ("KONVERSI MATA UANG\n","1. IDR\n","2. USD\n","3. SGD\n","4. EUR\n","5. JPY\n")
    awal = input ("APA MATA UANG AWAL ANDA? ")
    akhir = input ("MAU DI KONVERSIKAN KEMANA? ")
    print ("\n")

    if awal == "1":
        frt = input (f"{hi}\b{nama[0]}{ke}")
        break
    elif awal == "2":
        kop = input (f"{hi}\b{nama[1]}{ke}")
        frt = float(kop)*usd
        break
    elif awal == "3":
        kop = input (f"{hi}\b{nama[2]}{ke}")
        frt = float(kop)*sgd
        break
    elif awal == "4":
        kop = input (f"{hi}\b{nama[3]}{ke}")
        frt = float(kop)*eur
        break
    elif awal == "5":
        kop = input (f"{hi}\b{nama[4]}{ke}")
        frt = float(kop)*jpy
        break
    else :
        print ("FORMAT YANG ANDA MASUKKAN SALAH")

if akhir == "1":
    nilai = float(frt) / 1
    kl = nama[0]
if akhir == "2":
    nilai = float(frt)/float(usd)
    kl = nama[1]
if akhir == "3":
    nilai = float(frt)/float(sgd)
    kl = nama[2]
if akhir == "4":
    nilai = float(frt)/float(eur)
    kl = nama[3]
if akhir == "5":
    nilai = float(frt)/float(jpy)
    kl = nama [4]
ex = round(nilai, 2)
ribuan = f"{ex:,}"
print (f"{dalam}{ribuan}{kl}")
if ex == 0.0:
    print("\nitu duit atau harga diriku dimatamu sih? kok ga ada harganya banget")