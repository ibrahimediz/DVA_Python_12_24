import time

def zaman(fonk):
    def wrapper(*args,**kwargs):
        baslangic = time.time()
        sayi = fonk(*args,**kwargs)
        bitis = time.time()
        print(f"{fonk.__name__} çalışması için geçen süre {bitis-baslangic}")
        return sayi
    return wrapper
@zaman
def faktoriyel(sayi):
    time.sleep(1)
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc *=i
    return sonuc
print(faktoriyel(5))


