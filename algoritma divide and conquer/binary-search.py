def cari_biner(daftar_nilai, batas_bawah, batas_atas, nilai_cari):
    if batas_bawah > batas_atas:
        return -1
    
    titik_tengah = (batas_bawah + batas_atas) // 2
    
    if daftar_nilai[titik_tengah] == nilai_cari:
        return titik_tengah
    elif nilai_cari < daftar_nilai[titik_tengah]:
        return cari_biner(daftar_nilai, batas_bawah, titik_tengah - 1, nilai_cari)
    else:
        return cari_biner(daftar_nilai, titik_tengah + 1, batas_atas, nilai_cari)

kumpulan_data = [3, 7, 10, 15, 18, 23, 29, 35]
nilai_cari = 23

hasil_pencarian = cari_biner(kumpulan_data, 0, len(kumpulan_data) - 1, nilai_cari)

print("Nama: Raka Restu Saputra")
print("NIM: 247006111172 \n")
print(f"Array: {kumpulan_data}")
print(f"Target: {nilai_cari}")
if hasil_pencarian != -1:
    print(f"Hasil: Target ditemukan pada indeks: {hasil_pencarian}")
else:
    print("Hasil: Target tidak ditemukan")