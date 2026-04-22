def input_petugas():
    nama = input("Masukkan nama petugas: ")
    return nama

def input_buku():
    daftar = []

    for i in range(3):
        print(f"\nBuku ke-{i+1}")
        judul = input("Judul buku: ")

        while True:
            try:
                halaman = int(input("Jumlah halaman: "))
                break
            except ValueError:
                print("Harus berupa angka! Coba lagi.")

        daftar.append({
            "judul": judul,
            "halaman": halaman
        })

    return daftar