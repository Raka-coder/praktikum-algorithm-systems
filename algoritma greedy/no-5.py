# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x['profit'], reverse=True)
    
    max_d = max(job['deadline'] for job in jobs)
    
    slots = [None] * (max_d + 1)
    total_profit = 0
    scheduled_jobs = []

    for job in jobs:
        for j in range(job['deadline'], 0, -1):
            if slots[j] is None:
                slots[j] = job['id']
                total_profit += job['profit']
                scheduled_jobs.append(job['id'])
                break
                
    return slots[1:], total_profit

dataset = [
    {'id': 'J1', 'profit': 100, 'deadline': 2},
    {'id': 'J2', 'profit': 19, 'deadline': 1},
    {'id': 'J3', 'profit': 27, 'deadline': 2},
    {'id': 'J4', 'profit': 25, 'deadline': 1},
    {'id': 'J5', 'profit': 15, 'deadline': 3}
]

result_slots, max_profit = job_scheduling(dataset)

print(f"Urutan Job yang dijadwalkan: {result_slots}")
print(f"Total Keuntungan Maksimal: {max_profit}")