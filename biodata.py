asd = {"nama": "0","umur":"0","hobi":"0","agama":"0","jomblo":"0"}
asd["nama"] = input("MASUKKAN NAMA ANDA: ")
asd["nim"] = input("MASUKKAN NIM ANDA: ")
asd["umur"] = input("BERAPA UMUR ANDA?: ")
asd["hobi"] = input("SEPERTI APA HOBI ANDA?: ")
asd["agama"] = input("APA AGAMA ANDA?: ")
asd["jomblo"] = input("STATUS ANDA JOMBLO?(ya/tidak): ")
umur1 = int(asd["umur"])
nim1 = int(asd["nim"])

print ("\n" * 100)
print ("\n===================\nBIODATA ANDA SAAT INI\n===================\n")
print ("NAMA ANDA: "+ asd["nama"])
print (f"NIM ANDA: {nim1}")
print (f"UMUR ANDA: {umur1}")
print ("HOBI ANDA: "+asd["hobi"])
print ("AGAMA ANDA: "+asd["agama"])
print ("STATUS ANDA JOMBLO?: "+asd["jomblo"])

if asd["jomblo"] == "ya":
    print ("MASIH JOMBLO BRO? TURUT BERDUKA AKU BRO, MOGA JOMBLONYA GA TAMBAH LAMA")

elif asd["jomblo"] == "tidak" :
    print ("UDAH PUNYA PACAR? HIDIH NGAPAIIN ORANG PUNYA PACAR KESINI")

else :
    print ("STATUS ANDA SEKARANG: "+ asd["jomblo"])
