def input_petugas():
    nama = input("Masukkan nama petugas: ")
    return nama


def input_buku():
    daftar = []

    jumlah = int(input("Masukkan jumlah buku: "))

    for i in range(jumlah):
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


def tampilkan_data(petugas, daftar_buku):
    print("\n=== DATA PERPUSTAKAAN ===")
    print("Nama Petugas:", petugas)
    print("\nDaftar Buku:")

    for i, buku in enumerate(daftar_buku, start=1):
        print(f"{i}. {buku['judul']} - {buku['halaman']} halaman")


# ===== PROGRAM UTAMA =====
petugas = input_petugas()
data_buku = input_buku()
tampilkan_data(petugas, data_buku)