import datetime
import re

def increment_trip_id(trip_id):
    """Increments the numeric part of the trip ID by 1 (e.g., M-01 → M-02)."""
    match = re.search(r'(\d+)$', trip_id)
    if match:
        number_part = match.group(1)
        new_number = str(int(number_part) + 1).zfill(len(number_part))
        return trip_id[:-len(number_part)] + new_number
    else:
        raise ValueError("Trip ID must end with a numeric part, e.g., 'M-01'.")

# === User Inputs with Examples and Validation ===

try:
    start_time_input = input("Enter the starting time of the first trip (HH:MM:SS, e.g., 06:00:00): ")
    start_time = datetime.datetime.strptime(start_time_input, "%H:%M:%S")

    last_trip_start_time_input = input("Enter the starting time of the last trip (HH:MM:SS, e.g., 23:00:00): ")
    last_trip_start_time = datetime.datetime.strptime(last_trip_start_time_input, "%H:%M:%S")

    num_stops = int(input("Enter the number of stops (minimum 2, e.g., 3): "))
    if num_stops < 2:
        raise ValueError("You must enter at least 2 stops for a trip.")

    dwell_time = int(input("Enter the dwell time at each stop in seconds (minimum 0, e.g., 15): "))
    if dwell_time < 0:
        raise ValueError("Dwell time cannot be negative.")

    gap_time_minutes = int(input("Enter the gap time between trips in minutes (minimum 0, e.g., 10): "))
    if gap_time_minutes < 0:
        raise ValueError("Gap time cannot be negative.")
    gap_time = datetime.timedelta(minutes=gap_time_minutes)

    start_trip_id = input("Enter the starting trip ID (must end in a number, e.g., M-01): ")

    stop_ids = []
    for i in range(num_stops):
        stop_id = input(f"Enter stop ID for stop {i+1} (e.g., s-OLI-1-00{i+1}): ")
        stop_ids.append(stop_id)

    travel_times = []
    for i in range(num_stops - 1):
        seconds = int(input(f"Enter travel time (in seconds) from stop {i+1} to stop {i+2} (minimum 1, e.g., 120): "))
        if seconds < 1:
            raise ValueError("Travel time between stops must be at least 1 second.")
        travel_times.append(seconds)

except ValueError as e:
    print(f"\n Input Error: {e}")
    exit(1)

# === Generate GTFS Stop Times ===

gtfs_stop_times_day = []
current_trip_id = start_trip_id
current_time = start_time

while current_time <= last_trip_start_time:
    cumulative_time = datetime.timedelta(seconds=0)

    for stop_sequence in range(1, num_stops + 1):
        stop_id = stop_ids[stop_sequence - 1]
        stop_time = current_time + cumulative_time

        arrival_time = stop_time.strftime("%H:%M:%S")
        departure_time = (stop_time + datetime.timedelta(seconds=dwell_time)).strftime("%H:%M:%S")

        gtfs_stop_times_day.append([
            current_trip_id,
            arrival_time,
            departure_time,
            stop_id,
            stop_sequence
        ])

        # Add travel + dwell time for next leg (if not the last stop)
        if stop_sequence < num_stops:
            cumulative_time += datetime.timedelta(seconds=travel_times[stop_sequence - 1])
            cumulative_time += datetime.timedelta(seconds=dwell_time)

    # Move to next trip
    current_trip_id = increment_trip_id(current_trip_id)
    current_time += gap_time

# === Save GTFS stop_times.txt File ===

file_name = "stop_times.txt"
with open(file_name, "w") as file:
    file.write("trip_id,arrival_time,departure_time,stop_id,stop_sequence\n")
    for row in gtfs_stop_times_day:
        file.write(",".join(map(str, row)) + "\n")

print(f" stop_times.txt file has been successfully created.")

