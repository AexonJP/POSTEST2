print ("\n=========================\nSILAHKAN ISI BIODATA ANDA\n=========================\n")
asd = {"nama": "0","umur":"0","hobi":"0","agama":"0","jomblo":"0","berat":"0"}
asd["nama"] = input("MASUKKAN NAMA ANDA: ")
asd["nim"] = input("MASUKKAN NIM ANDA: ")
asd["umur"] = input("BERAPA UMUR ANDA?: ")
asd["hobi"] = input("APA HOBI ANDA?: ")
asd["agama"] = input("APA AGAMA ANDA?: ")
asd["berat"] = input("BERAPA BERAT ANDA SEKARANG: ")
asd["jomblo"] = input("STATUS ANDA JOMBLO?(ya/tidak): ")
umur1 = int(asd["umur"])
nim1 = int(asd["nim"])
berat1 = float(asd["berat"])

print ("\n=========================\nBIODATA ANDA SAAT INI\n=========================\n")
print ("NAMA ANDA: "+ asd["nama"])
print (f"NIM ANDA: {nim1}")
print (f"UMUR ANDA: {umur1}")
print ("HOBI ANDA: "+asd["hobi"])
print ("AGAMA ANDA: "+asd["agama"])
print (f"BERAT BADAN ANDA : {berat1} kg")

if asd["jomblo"] == "ya":
    ("STATUS ANDA JOMBLO?: "+asd["jomblo"])
    print ("MASIH JOMBLO BRO? TURUT BERDUKA AKU BRO, MOGA JOMBLONYA GA TAMBAH LAMA")

elif asd["jomblo"] == "tidak" :
    ("STATUS ANDA JOMBLO?: "+asd["jomblo"])
    print ("UDAH PUNYA PACAR? HIDIH NGAPAIIN ORANG PUNYA PACAR KESINI")

else :
    print ("STATUS ANDA SEKARANG: "+ asd["jomblo"])
