# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

def fractional_knapsack(items, capacity):
    for item in items:
        item['ratio'] = item['value'] / item['weight']
    
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    knapsack_content = []

    for item in items:
        if remaining_capacity <= 0:
            break
            
        if item['weight'] <= remaining_capacity:
            
            remaining_capacity -= item['weight']
            total_value += item['value']
            knapsack_content.append((item['name'], 1.0)) 
        else:
           
            fraction = remaining_capacity / item['weight']
            total_value += item['value'] * fraction
            knapsack_content.append((item['name'], round(fraction, 2)))
            remaining_capacity = 0
            
    return total_value, knapsack_content

capacity = 50
dataset = [
    {'name': 'I1', 'value': 60, 'weight': 10},
    {'name': 'I2', 'value': 100, 'weight': 20},
    {'name': 'I3', 'value': 120, 'weight': 30}
]

max_val, content = fractional_knapsack(dataset, capacity)

print(f"Total Nilai Maksimal: {max_val}")
print("Isi Tas (Item, Bagian):")
for item in content:
    print(item)