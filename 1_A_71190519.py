print("======== Calculator sederhana ========")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat \n")
menu = int(input("Masukkan pilihan: "))
b1 = int(input("Masukkan bilangan 1: "))
b2 = int(input("Masukkan bilangan 2: "))

#perhitungan
def calculator(menu):
    if (menu == 1):
        print("Hasilnya:", tambah(b1, b2))
    elif (menu == 2):
        print("Hasilnya:", kurang(b1, b2))
    elif (menu == 3):
        print("Hasilnya:", kali(b1, b2))
    elif (menu == 4):
        print("Hasilnya:", bagi(b1, b2))
    elif (menu == 5):
        print("Hasilnya:", pangkat(b1, b2))
    else:
        print("Hasilnya: Maaf input operasi antara 1-5")

#menghitung pertambahan
def tambah(b1, b2):
    tambah = b1 + b2
    return tambah

#menghitung pengurangan
def kurang(b1, b2):
    kurang = b1 - b2
    return kurang

#menghitung perkalian
def kali(b1, b2):
    kali = b1 * b2
    return kali

#menghitung pembagian
def bagi(b1, b2):
    bagi = b1 / b2
    return bagi

#menghitung pangkat
def pangkat(b1, b2):
    pangkat = b1 ** b2
    return pangkat


calculator(menu)
