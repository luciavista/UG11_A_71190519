def ambildanbalik(huruf, mulai, akhir, valid):
    if(valid):
        hasil = huruf[mulai-1:akhir]
        return(hasil[:: -1])
    elif(not valid):
        return(huruf[mulai-1:akhir])
    else:
        print("Maaf terjadi kesalahan")


print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))
