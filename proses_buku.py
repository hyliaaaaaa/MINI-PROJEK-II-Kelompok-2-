def hitung_total(daftar_buku):
    total = 0
    for buku in daftar_buku:
        total += buku["halaman"]
    return total

def cari_terbanyak(daftar_buku):
    terbanyak = daftar_buku[0]

    for buku in daftar_buku:
        if buku["halaman"] > terbanyak["halaman"]:
            terbanyak = buku

    return terbanyak

def hitung_rata_rata(daftar_buku):
    total = hitung_total(daftar_buku)
    rata = total / len(daftar_buku)
    return rata