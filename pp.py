n = int(input("Masukkan banyaknya elemen: "))
array = []

for i in range(n):
    nilai = int(input("Masukkan nilai elemen {}: ".format(i+1)))
    array.index(nilai)

print("Array: ", array)