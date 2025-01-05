def hitung_faktorial(n):
    faktorial = 1

    # Perulangan for untuk mengalikan angka dari 1 hingga n
    for i in range(1, n + 1):
        faktorial *= i

    return faktorial
