from input_buku import input_petugas, input_buku
from proses_buku import hitung_total_halaman, cari_buku_terbanyak

def main():
    print("=== APLIKASI DATA BUKU ===\n")

    # input
    nama = input_petugas()
    daftar_buku = input_buku()

    # proses
    total = hitung_total_halaman(daftar_buku)
    terbanyak = cari_buku_terbanyak(daftar_buku)

    # output
    print("\n=== HASIL DATA ===")
    print(f"Petugas       : {nama}")
    print("\nDaftar Buku:")
    
    for i, buku in enumerate(daftar_buku, start=1):
        print(f"{i}. {buku['judul']} ({buku['halaman']} halaman)")

    print(f"\nTotal Halaman : {total}")
    print(f"Buku Terbanyak: {terbanyak['judul']} ({terbanyak['halaman']} halaman)")

if __name__ == "__main__":
    main()