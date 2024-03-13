# Data dictionary pertama: jadwal DasproIF2
jadwal_daspro_if2 = {
    "Senin": "Dasar Pemrograman 2",
    "Selasa": "Dasar Pemrograman 2",
    "Rabu": "Dasar Pemrograman 2",
    "Kamis": "Dasar Pemrograman 2",
    "Jumat": "Dasar Pemrograman 2"
}

# Data dictionary kedua: jadwal DasproIF3
jadwal_daspro_if3 = {
    "Senin": "Dasar Pemrograman 3",
    "Selasa": "Dasar Pemrograman 3",
    "Rabu": "Dasar Pemrograman 3",
    "Kamis": "Dasar Pemrograman 3",
    "Jumat": "Dasar Pemrograman 3"
}

# Menggabungkan kedua data dictionary
jadwal_gabungan = {}
for hari in jadwal_daspro_if2:
    jadwal_gabungan[hari] = (jadwal_daspro_if2[hari], jadwal_daspro_if3[hari])

# Menampilkan jadwal gabungan
print("Jadwal Gabungan DasproIF2 dan DasproIF3:")
for hari in jadwal_gabungan:
    print(f"{hari}: DasproIF2 - {jadwal_gabungan[hari][0]}, DasproIF3 - {jadwal_gabungan[hari][1]}")
