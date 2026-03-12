def gcd(a, b, steps=0):
    steps += 1
    if b == 0:
        print(f"Step {steps}: b = 0")
        return a, steps
    
    print(f"Step {steps}: Hitung GCD({b}, {a} mod {b} = {a % b})")
    return gcd(b, a % b, steps)

a, b = 48, 18

print("\nNama : Raka Restu Saputra")
print("NIM  : 247006111172\n")
print(f"Mencari GCD dari {a} dan {b}")
result_gcd, total_steps = gcd(a, b)
print(f"\nGCD ditemukan = {result_gcd}")
print(f"Total langkah rekursi: {total_steps}")