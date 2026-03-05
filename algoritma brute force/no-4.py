# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

import itertools

def brute_force_password(alphabet, target, length):
    total_checked = 0
    for combo in itertools.product(alphabet, repeat=length):
        total_checked += 1
        password = ''.join(combo)
        if password == target:
            return password, total_checked
    return None, total_checked

alphabet = ['a', 'b', 'c', '1', '2']
target = "b1a"
length = 3

found, attempts = brute_force_password(alphabet, target, length)

print("Password ditemukan:", found)
print("Percobaan ke:", attempts)
print("Total kombinasi diperiksa:", len(alphabet)**length)
