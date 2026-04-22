from input_buku import input_petugas, input_buku
from proses_buku import hitung_total_halaman, cari_buku_terbanyak, hitung_rata_rata


def main():
    print("=== APLIKASI DATA BUKU ===")

    nama_petugas = input_petugas()
    daftar_buku = input_buku()

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


if __name__ == "_main_":
    main()