# GTFS Feed Automation Scripts  

## 📌 Overview  
This directory contains Python scripts to automate the generation of GTFS transit feed files for the **Islamabad Orange Line Metro Bus**. These scripts generate key GTFS files like `stop_times.txt` and `trips.txt`, reducing manual effort in transit schedule digitization.  

## 📂 Scripts in This Directory  

1. **`trips.py`**  
   - Generates the `trips.txt` file for GTFS.  
   - Allows users to input route details and automatically assigns trip IDs.  
   - Supports custom trip headsigns, service IDs, and direction IDs.  

2. **`stops_times.py`**  
   - Generates the `stop_times.txt` file.  
   - Allows users to input trip start times, stop IDs, dwell times, and total trip duration.  
   - Automatically calculates arrival and departure times for all stops.  

## 🚀 How to Run the Scripts  

### **🔹 Running `trips.py`**  
 Open a terminal and navigate to the `code/` directory:  
   cd code
###Run the script:
python trips.py
Follow the prompts to input transit details.
The generated trips.txt file will be saved in the same directory.
🔹 Running stops_times.py
###
Run the script:
python stops_times.py

Input the required details, such as start times, stop IDs, and dwell times.
The generated stop_times.txt file will be saved in the same directory.
###
📝 Output Files
trips.txt → Contains trip schedules with route and service information.
stop_times.txt → Lists arrival and departure times for each stop along the route.
###
Requirements
Python 3.x
No additional dependencies (standard Python libraries used).
###
📧 Contact
For questions or contributions, contact: muawiairfan11@gmail.com
