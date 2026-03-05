# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

def string_match_bf(text, pattern):
    n = len(text)
    m = len(pattern)
    indices = []
    total_comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            total_comparisons += 1 
            if text[i + j] == pattern[j]:
                j += 1
            else:
                break
        if j == m:
            indices.append(i)
            
    return indices, total_comparisons

teks = "ALGORITMASTRATEGIALGORITMA"
pattern = "RIT"

hasil_indeks, jumlah_cek = string_match_bf(teks, pattern)

print(f"Indeks kemunculan: {hasil_indeks}")
print(f"Total perbandingan karakter: {jumlah_cek}")