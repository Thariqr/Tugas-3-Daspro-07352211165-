def lists_to_dict(keys, values):
    # Pastikan panjang kedua list sama
    if len(keys) != len(values):
        print("Error: Panjang list kunci dan list nilai harus sama.")
        return None
    
    # Buat dictionary kosong
    result_dict = {}
    
    # Masukkan pasangan kunci-nilai ke dalam dictionary
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    
    return result_dict

# Contoh list
keys_list = ["nama", "umur", "tempat lahir", "olahraga kesukaan"]
values_list = ["thariqramadhan",21 , "ternate", "berenang"]

# Panggil fungsi untuk mengonversi list menjadi dictionary
result_dict = lists_to_dict(keys_list, values_list)

# Cetak hasilnya
print("Hasil konversi:")
print(result_dict)
