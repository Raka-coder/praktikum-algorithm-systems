def urutkan_gabung(larik_data):
    if len(larik_data) <= 1:
        return larik_data
    
    titik_tengah = len(larik_data) // 2
    bagian_kiri = urutkan_gabung(larik_data[:titik_tengah])
    bagian_kanan = urutkan_gabung(larik_data[titik_tengah:])
    
    return gabungkan_bagian(bagian_kiri, bagian_kanan)

def gabungkan_bagian(bagian_kiri, bagian_kanan):
    hasil_gabung = []
    idx_kiri = idx_kanan = 0
    
    while idx_kiri < len(bagian_kiri) and idx_kanan < len(bagian_kanan):
        if bagian_kiri[idx_kiri] < bagian_kanan[idx_kanan]:
            hasil_gabung.append(bagian_kiri[idx_kiri])
            idx_kiri += 1
        else:
            hasil_gabung.append(bagian_kanan[idx_kanan])
            idx_kanan += 1
            
    hasil_gabung.extend(bagian_kiri[idx_kiri:])
    hasil_gabung.extend(bagian_kanan[idx_kanan:])
    return hasil_gabung

data_mentah = [38, 27, 43, 3, 9, 82, 10]

data_terurut = urutkan_gabung(data_mentah)

print("Nama: Raka Restu Saputra")
print("NIM: 247006111172 \n")
print(f"Data Awal: {data_mentah}")
print(f"Hasil Sorting: {data_terurut}")