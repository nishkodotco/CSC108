total_seconds = 95399
total_hours = total_seconds // (60 * 60)

remaining_seconds = total_seconds % ( 60 * 60)

total_minutes = remaining_seconds // 60
remaining_seconds = remaining_seconds % 60

print("hours: ", total_hours)
print("minutes: ", total_minutes)
print("seconds: ", remaining_seconds)
