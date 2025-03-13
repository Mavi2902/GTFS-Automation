Automating GTFS Feed Creation for Islamabad’s Orange Line Metro Bus
📌 Overview
This repository contains the GTFS automation scripts and the JOSS research paper for generating transit feeds for Islamabad’s Orange Line Metro Bus. The project streamlines the creation of stop_times.txt and trips.txt files while allowing transit agencies to manually input static data for seamless GTFS integration.

📂 Repository Structure
code/ → Contains Python scripts for GTFS automation, dependencies, and the license.
paper/ → Includes the paper.md file, images, and bibliography for JOSS submission.
🚀 Getting Started
🔹 Installation
To set up the project, clone the repository
git clone [https://github.com/Mavi2902/GTFS-Automation.git]

🔹 Running the GTFS Automation Script
To generate the GTFS feed:


python generate_gtfs.py --input data/schedules --output gtfs_feed/
This will create stop_times.txt and trips.txt files.

🛠 Software Availability
The GTFS automation scripts are available under the MIT License.
👉 GitHub Repository: [https://github.com/Mavi2902/GTFS-Automation.git]

📄 Research Paper
This work has been submitted to the Journal of Open Source Software (JOSS).
👉 The full paper is available in the paper/ directory as paper.md.

🤝 Contributing
If you'd like to contribute, please fork the repository and submit a pull request.

📧 Contact
For questions or collaborations, contact: muawiairfan11@gmail.com
