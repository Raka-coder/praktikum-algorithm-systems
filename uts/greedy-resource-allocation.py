print("Nama : Raka Restu Saputra")
print("NPM  : 247006111172\n")


def solve_greedy_allocation():
    a, b, c = 1, 7, 2
    capacity = 20 + a + b
    apps = []
    
    print(f"Kapasitas CPU Server: {capacity} unit\n")
    
    for i in range(1, 14):
        cpu = ((i * a + c) % 10) + 1
        profit = ((i * b + a * c) % 50) + 10
        apps.append({'id': i, 'cpu': cpu, 'profit': profit, 'ratio': profit/cpu})
    
    apps_sorted = sorted(apps, key=lambda x: x['ratio'], reverse=True)

    total_profit = 0
    selected_apps = []
    remaining_capacity = capacity
    selected_data = []

    for app in apps_sorted:
        if app['cpu'] <= remaining_capacity:
            remaining_capacity -= app['cpu']
            total_profit += app['profit']
            selected_apps.append(app['id'])
            selected_data.append(app)

    print("=" * 70)
    print("URUTAN BERDASARKAN RASIO      |    PROSES SELEKSI GREEDY")
    print("=" * 70)
    print("ID  | CPU | Profit | Rasio    ||    ID  | CPU | Profit | Sisa CPU")
    print("-" * 70)
    
    for i in range(len(apps_sorted)):
        app = apps_sorted[i]
        
        selected = app in selected_data
        sisa = ""
        
        if i < len(selected_data):
            selected_app = selected_data[i]
            if selected_app['id'] == app['id']:
                sisa = f"{remaining_capacity + selected_app['cpu']:2d} → {remaining_capacity:2d}"
        
        if sisa:
            print(f"{app['id']:2d}  | {app['cpu']:3d} | {app['profit']:5d} | {app['ratio']:6.2f}    ||    {app['id']:2d}  | {app['cpu']:3d} | {app['profit']:5d} | {sisa:>9s}")
        else:
            print(f"{app['id']:2d}  | {app['cpu']:3d} | {app['profit']:5d} | {app['ratio']:6.2f}    ||        -    -        -")
    
    print("-" * 70)
    print(f"\nAplikasi yang dipilih: {sorted(selected_apps)}")
    print(f"Total Profit Maksimum: {total_profit}")
    print(f"Sisa kapasitas CPU: {remaining_capacity} unit")

solve_greedy_allocation()