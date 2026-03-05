# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

def activity_selection(activities):
    activities.sort(key=lambda x: x[2])
    
    selected_activities = [activities[0]]
    last_finish_time = activities[0][2]
    
    for i in range(1, len(activities)):
        start_time = activities[i][1]
        if start_time >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][2]
            
    return selected_activities

dataset = [
    ("A1", 1, 4),
    ("A2", 3, 5),
    ("A3", 0, 6),
    ("A4", 5, 7),
    ("A5", 8, 9)
]

result = activity_selection(dataset)

print("Aktivitas yang dipilih (Nama, Start, Finish):")
for act in result:
    print(act)
print(f"Total aktivitas maksimum: {len(result)}")