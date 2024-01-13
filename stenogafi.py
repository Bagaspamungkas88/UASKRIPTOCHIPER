from stegano import lsb

# Ganti path gambar sesuai dengan path lengkapnya
path_gambar = r"D:/semester 5/kriptografi/ruang.png"

# Menyembunyikan pesan dalam gambar
secret = lsb.hide(path_gambar, "mohon maaf terlambat karena habis debat pilpress")

# Menyimpan gambar yang telah dimodifikasi
secret.save(r"D:/semester 5/kriptografi/perruang.png")

# Mencetak pesan yang disembunyikan
print(lsb.reveal(r"D:/semester 5/kriptografi/perruang.png"))