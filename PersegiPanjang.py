class PersegiPanjang:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
    def HitungKeliling(self):
        return 2 * (self.panjang+self.lebar)
    def HitungLuas(self):
        return self.panjang * self.lebar

p=float(input('Masukkan Panjang : '))
l=float(input('Masukkan Lebar : '))

meja = PersegiPanjang(p,l)

keliling = meja.HitungKeliling()
luas = meja.HitungLuas()

print('Keliling = ',keliling)
print('Luas = ',luas)
