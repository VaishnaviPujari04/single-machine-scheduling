import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Sort all tasks by due date (Earliest Due Date rule)
df_sorted = df.sort_values(by='due_date')

# Schedule each task
current_time = 0
schedule = []

for index, row in df_sorted.iterrows():
    start_time = current_time
    end_time = start_time + row['processing_time']
    schedule.append({
        'job_id': row['job_id'],
        'task_id': row['task_id'],
        'start_time': start_time,
        'end_time': end_time,
        'due_date': row['due_date'],
        'lateness': max(0, end_time - row['due_date'])
    })
    current_time = end_time

# Show schedule
schedule_df = pd.DataFrame(schedule)
print(schedule_df)

# Calculate total lateness
total_lateness = schedule_df['lateness'].sum()
print(f"\nTotal Lateness: {total_lateness}")
