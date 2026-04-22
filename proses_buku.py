def hitung_total_halaman(daftar_buku):
    total = 0
    for buku in daftar_buku:
        total += buku["halaman"]
    return total


def cari_buku_terbanyak(daftar_buku):
    terbanyak = daftar_buku[0]

    for buku in daftar_buku:
        if buku["halaman"] > terbanyak["halaman"]:
            terbanyak = buku

    return terbanyak