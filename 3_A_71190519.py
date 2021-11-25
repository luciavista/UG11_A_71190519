kalimat = input("Masukkan Kalimat: ")
start = int(input("Index Start: "))
stop = int(input("Index Stop: "))

#perhitungan berupa kalimat, start, stop
def hitung_hapus(kalimat, start, stop):
    hitung_start = len(kalimat)
    hitung_stop = len(kalimat[start-1:stop])
    persentase = (hitung_stop / hitung_start) * 100
    return persentase


print(hitung_hapus(kalimat, start, stop))
