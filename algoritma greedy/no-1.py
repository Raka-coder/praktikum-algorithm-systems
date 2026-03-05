# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    result = []
    remaining = amount
    
    for coin in coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
            
    return result

available_coins = [1, 5, 10, 25]
target_value = 68

solution = coin_change_greedy(available_coins, target_value)

print(f"Target Uang: {target_value}")
print(f"Koin Tersedia: {available_coins}")
print(f"Koin yang dipilih: {solution}")
print(f"Total Koin Minimum: {len(solution)}")