class KonversiSuhu: #nama class
    #methode constructor
    def __init__(self,suhu_celcius, ):
        self.suhu_celcius = suhu_celcius

    #memuat methode HitungFahrenheit
    def celcius_to_fahrenheit(self):
        return (self.suhu_celcius * 9/5)+32

    #memuat methode HitungReamur
    def celcius_to_reamur(self):
        return self.suhu_celcius * 4/5

    # memuat methode HitungKelvin
    def celcius_to_kelvin(self):
        return self.suhu_celcius + 237.15

#bagian input
suhu_celcius = float(input("Masukkan suhu dalam Celcius : "))

#membuat object
konveter = KonversiSuhu(suhu_celcius)

#memanggil method Menghitung suhu dalam Fahrenheit, Reamur, dan Kelvin
print("fahrenheit : ", konveter.celcius_to_fahrenheit())
print("reamur : ", konveter.celcius_to_reamur())
print("kelvin : ", konveter.celcius_to_kelvin())