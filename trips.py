import csv
import re

# Function to standardize the trip headsign
def standardize_headsign(headsign):
    return headsign.lower().strip()

# Function to extract the numeric part and its width from trip_id
def extract_numeric_trip_id(trip_id):
    match = re.search(r'(\d+)$', trip_id)
    if match:
        return int(match.group()), len(match.group())
    else:
        raise ValueError(f"Invalid trip_id format: {trip_id}")

# Function to generate trips based on input pattern
def generate_trips(route_id, service_id, headsigns, num_trips, block_ids, shape_ids, first_trip_id):
    trips_data = []
    
    # Extract numeric part of the trip_id and its width
    try:
        trip_counter, num_width = extract_numeric_trip_id(first_trip_id)
    except ValueError as e:
        print(e)
        return []
    
    trip_base = first_trip_id[:-num_width]  # Strip numeric part to get base
    
    for idx, headsign in enumerate(headsigns):
        standardized_headsign = standardize_headsign(headsign)
        for trip_num in range(num_trips[idx]):
            trip_id = f"{trip_base}{trip_counter:0{num_width}d}"
            trips_data.append({
                "trip_id": trip_id,
                "route_id": route_id,
                "service_id": service_id,
                "trip_headsign": standardized_headsign,
                "direction_id": str(idx),
                "block_id": block_ids[idx] if idx < len(block_ids) else "0",
                "shape_id": shape_ids[idx] if idx < len(shape_ids) else "0"
            })
            trip_counter += 1
    return trips_data

# Function to write the trips data to a trips.txt file
def write_trips_file(trips_data, file_name='trips.txt'):
    fieldnames = [
        "route_id",
        "service_id",
        "trip_id",
        "trip_headsign",
        "direction_id",
        "block_id",
        "shape_id"
    ]

    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for trip in trips_data:
            writer.writerow(trip)

    print(f"{file_name} generated successfully.")

# Main function to handle user input and generate trips
def main():
    # Input number of routes
    num_routes = int(input("Enter the number of routes: "))
    
    all_trips_data = []
    
    for route_idx in range(num_routes):
        print(f"\n--- Route {route_idx + 1} ---")
        
        # Input Parameters for each route
        route_id = input("Enter route_id: ")
        service_id = input(f"Enter service_id for {route_id}: ")
        first_trip_id = input(f"Enter the first trip_id for {route_id}: ")
        headsigns = input(f"Enter trip headsigns for {route_id} (comma-separated): ").split(',')
        num_trips = list(map(int, input(f"Enter number of trips for each headsign for {route_id} (comma-separated): ").split(',')))
        
        # Optional parameters
        block_ids = input(f"Enter block_ids for each headsign for {route_id} (comma-separated, leave blank if not used): ").split(',')
        shape_ids = input(f"Enter shape_ids for each headsign for {route_id} (comma-separated, leave blank if not used): ").split(',')
        
        # Remove empty values from optional parameters
        block_ids = [block_id.strip() for block_id in block_ids if block_id.strip()]
        shape_ids = [shape_id.strip() for shape_id in shape_ids if shape_id.strip()]

        # Generate the trips for this route
        trips_data = generate_trips(route_id, service_id, headsigns, num_trips, block_ids, shape_ids, first_trip_id)
        
        if trips_data:
            # Append the trips to the overall list
            all_trips_data.extend(trips_data)
    
    if all_trips_data:
        # Write all trips data to trips.txt file
        write_trips_file(all_trips_data)

if __name__ == "__main__":
    main()

