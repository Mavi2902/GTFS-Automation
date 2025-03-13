import datetime
import re

def increment_trip_id(trip_id):
    """Increments the numeric part of the trip ID by 1."""
    match = re.search(r'(\d+)$', trip_id)
    if match:
        number_part = match.group(1)
        new_number = str(int(number_part) + 1).zfill(len(number_part))
        return trip_id[:-len(number_part)] + new_number
    else:
        raise ValueError("No numeric part found in the trip ID.")

# User inputs
start_time_input = input("Enter the starting time of the first trip (HH:MM:SS, e.g., 06:00:00): ")
start_time = datetime.datetime.strptime(start_time_input, "%H:%M:%S")

last_trip_start_time_input = input("Enter the starting time of the last trip (HH:MM:SS, e.g., 23:00:00): ")
last_trip_start_time = datetime.datetime.strptime(last_trip_start_time_input, "%H:%M:%S")

num_stops = int(input("Enter the number of stops (e.g., 2): "))

dwell_time = int(input("Enter the dwell time at each stop in seconds (e.g., 15): "))

total_trip_time_minutes = int(input("Enter the total time required for one trip in minutes (e.g., 10): "))
total_trip_time = datetime.timedelta(minutes=total_trip_time_minutes)

gap_time_minutes = int(input("Enter the gap time between trips in minutes (e.g., 10): "))
gap_time = datetime.timedelta(minutes=gap_time_minutes)

start_trip_id = input("Enter the starting trip ID (e.g., M-01): ")

stop_ids = [input(f"Enter the stop ID for stop {i+1} (e.g., s-01-001): ") for i in range(num_stops)]

# Calculate the interval between stops
stop_interval = total_trip_time / (num_stops - 1)

# Initialize the list for GTFS stop times
gtfs_stop_times_day = []

current_trip_id = start_trip_id
current_time = start_time

# Generate the schedule
while current_time <= last_trip_start_time:
    for stop_sequence in range(1, num_stops + 1):
        stop_id = stop_ids[stop_sequence - 1]

        # Calculate the time at this stop
        stop_time = current_time + (stop_interval * (stop_sequence - 1))

        arrival_time = stop_time.strftime("%H:%M:%S")
        departure_time = (stop_time + datetime.timedelta(seconds=dwell_time)).strftime("%H:%M:%S")

        gtfs_stop_times_day.append([current_trip_id, arrival_time, departure_time, stop_id, stop_sequence])

    # Increment the trip ID for the next trip
    current_trip_id = increment_trip_id(current_trip_id)
    
    # Move to the next trip's start time by adding the gap to the start time of the first trip
    current_time = current_time + gap_time

# Save the stop_times.txt file
file_name = "stop_times_day.txt"
with open(file_name, "w") as file:
    file.write("trip_id,arrival_time,departure_time,stop_id,stop_sequence\n")
    for stop_time_day in gtfs_stop_times_day:
        file.write(",".join(map(str, stop_time_day)) + "\n")

print(f"Stop times for trips have been saved to '{file_name}' in the current directory.")
