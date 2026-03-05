def hitung_lintas_maksimum(deret_angka, indeks_awal, indeks_tengah, indeks_akhir):

    jumlah_kiri = -float('inf')
    jumlah_saat_ini = 0
    for i in range(indeks_tengah, indeks_awal - 1, -1):
        jumlah_saat_ini += deret_angka[i]
        if jumlah_saat_ini > jumlah_kiri:
            jumlah_kiri = jumlah_saat_ini
            
    jumlah_kanan = -float('inf')
    jumlah_saat_ini = 0
    for i in range(indeks_tengah + 1, indeks_akhir + 1):
        jumlah_saat_ini += deret_angka[i]
        if jumlah_saat_ini > jumlah_kanan:
            jumlah_kanan = jumlah_saat_ini
            
    return jumlah_kiri + jumlah_kanan

def cari_subarray_maksimal(deret_angka, indeks_awal, indeks_akhir):
    if indeks_awal == indeks_akhir:
        return deret_angka[indeks_awal]
    
    indeks_tengah = (indeks_awal + indeks_akhir) // 2
    
    maksimum_kiri = cari_subarray_maksimal(deret_angka, indeks_awal, indeks_tengah)
    maksimum_kanan = cari_subarray_maksimal(deret_angka, indeks_tengah + 1, indeks_akhir)
    maksimum_lintas = hitung_lintas_maksimum(deret_angka, indeks_awal, indeks_tengah, indeks_akhir)
    
    return max(maksimum_kiri, maksimum_kanan, maksimum_lintas)

sampel_data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

hasil_maksimum = cari_subarray_maksimal(sampel_data, 0, len(sampel_data) - 1)

print("Nama: Raka Restu Saputra")
print("NIM: 247006111172 \n")
print(f"Array: {sampel_data}")
print(f"Jumlah Subarray Maksimum: {hasil_maksimum}")