def hitung_total(daftar_buku):
    total = 0
    for buku in daftar_buku:
        total += buku["halaman"]
    return total

<<<<<<< HEAD
def main():
    print("=== APLIKASI DATA BUKU ===")
=======
def cari_terbanyak(daftar_buku):
    terbanyak = daftar_buku[0]

    for buku in daftar_buku:
        if buku["halaman"] > terbanyak["halaman"]:
            terbanyak = buku
>>>>>>> 66a8d77636355324a1b2fa26ab0e817fd0d96230

    return terbanyak

<<<<<<< HEAD
    total = hitung_total_halaman(daftar_buku)
    buku_terbanyak = cari_buku_terbanyak(daftar_buku)
    rata_rata = hitung_rata_rata(daftar_buku)

    print("\n=== HASIL DATA ===")
    print(f"Petugas: {nama_petugas}")

    print("\nDaftar Buku:")
    for i, buku in enumerate(daftar_buku, start=1):
        print(f"{i}. {buku['judul']} ({buku['halaman']} halaman)")

    print(f"\nTotal Halaman: {total}")
    print(f"Rata-rata Halaman: {rata_rata:.2f}")
    print(f"Buku dengan halaman terbanyak: {buku_terbanyak['judul']} ({buku_terbanyak['halaman']} halaman)")

if __name__ == "__main__":
    main()
=======
def hitung_rata_rata(daftar_buku):
    total = hitung_total(daftar_buku)
    rata = total / len(daftar_buku)
    return rata
>>>>>>> 66a8d77636355324a1b2fa26ab0e817fd0d96230
