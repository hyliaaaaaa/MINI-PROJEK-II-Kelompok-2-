from input_buku import input_petugas, input_buku
from proses_buku import hitung_total, cari_terbanyak, hitung_rata_rata


def main():
    print("=== APLIKASI DATA BUKU ===\n")

    # input
    nama_petugas = input_petugas()
    daftar_buku = input_buku()

    # proses
    total = hitung_total(daftar_buku)
    buku_terbanyak = cari_terbanyak(daftar_buku)
    rata_rata = hitung_rata_rata(daftar_buku)

    # output
    print("\n=== HASIL DATA ===")
    print(f"Petugas: {nama_petugas}")

    print("\nDaftar Buku:")
    for i, buku in enumerate(daftar_buku, start=1):
        print(f"{i}. {buku['judul']} ({buku['halaman']} halaman)")

    print(f"\nTotal Halaman : {total}")
    print(f"Rata-rata     : {rata_rata:.2f}")
    print(f"Buku Terbanyak: {buku_terbanyak['judul']} ({buku_terbanyak['halaman']} halaman)")


if __name__ == "__main__":
    main()