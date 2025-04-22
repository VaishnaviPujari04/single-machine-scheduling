import pandas as pd
import matplotlib.pyplot as plt

# Read or reuse the result DataFrame (example data)
schedule = [
    {'job_id': 'J3', 'task_id': 'T1', 'start_time': 0, 'end_time': 1},
    {'job_id': 'J1', 'task_id': 'T1', 'start_time': 1, 'end_time': 4},
    {'job_id': 'J4', 'task_id': 'T1', 'start_time': 4, 'end_time': 9},
    {'job_id': 'J2', 'task_id': 'T1', 'start_time': 9, 'end_time': 13},
    {'job_id': 'J5', 'task_id': 'T1', 'start_time': 13, 'end_time': 15},
    {'job_id': 'J3', 'task_id': 'T2', 'start_time': 15, 'end_time': 17},
    {'job_id': 'J1', 'task_id': 'T2', 'start_time': 17, 'end_time': 19},
    {'job_id': 'J2', 'task_id': 'T2', 'start_time': 19, 'end_time': 22},
]

df = pd.DataFrame(schedule)

# Assign a unique color for each job_id
job_colors = {job_id: f"C{i}" for i, job_id in enumerate(df['job_id'].unique())}

# Create a figure
plt.figure(figsize=(10, 5))

for idx, row in df.iterrows():
    plt.barh(
        y=row['job_id'],
        width=row['end_time'] - row['start_time'],
        left=row['start_time'],
        height=0.4,
        color=job_colors[row['job_id']],
        edgecolor='black'
    )
    plt.text(
        x=(row['start_time'] + row['end_time']) / 2,
        y=row['job_id'],
        s=row['task_id'],
        va='center',
        ha='center',
        color='white',
        fontsize=9,
        fontweight='bold'
    )

plt.xlabel('Time')
plt.ylabel('Jobs')
plt.title('Single Machine Scheduling - Gantt Chart')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
