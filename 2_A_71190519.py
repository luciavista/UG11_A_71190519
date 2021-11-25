#mengambil 1 huruf ditengah
def ambil_tengah(huruf, tambah=0):
    if(tambah):
        hitung = len(huruf)
        bagi = (hitung//2)
        return(huruf[bagi+tambah])
    else:
        hitung = len(huruf)
        bagi = (hitung//2)
        return(huruf[bagi])

#test case
print(ambil_tengah("abcdefg", 1))
print(ambil_tengah("abcdefg", 2))
print(ambil_tengah("abcd"))
