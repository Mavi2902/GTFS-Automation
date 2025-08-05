**Automating GTFS Feed Generation for Public** **Transit: A Case Study of Islamabad's Orange Line**



authors:
  - name: "Muawia Irfan"
    affiliation: "Department of Computer Science, Quaid-i-Azam University, Islamabad"
    orcid: "https://orcid.org/0009-0004-7968-3592"
    corresponding: true

  - name: "Irfan-ul-Haq Qureshi"
    affiliation: "Department of Computer Science, Quaid-i-Azam University, Islamabad"
    orcid: ""

  - name: ""
    affiliation: ""
    orcid: ""

  - name: ""
    affiliation: ""
    orcid: ""

  - name: ""
    affiliation: ""
    orcid: ""

date: 5 August 2025

bibliography: paper.bib

tags:
  - GTFS
  - public transportation
  - Python
  - transit data automation
  - urban mobility


## Summary

Public transportation is the backbone of urban mobility, its efficiency depends on how easily it is accessible and useful transit information. General Transit Feed Specification (GTFS) provides a structured data format for representing the schedules and spatial information of public transportation systems. This method makes public transportation information easier to integrate and share through digital platforms like Google Maps, enhancing commuters' access. This paper describes the Orange Line Metro Bus in Islamabad's GTFS installation, a significant step toward updating the city's transit system by digitizing transit data. In contrast to the labor-intensive manual transcription of schedules, or a fully automated solution that may be complex to set up, we propose a semi-automated scripting approach that is efficient, simple, and easy to adopt by public transit authorities. Our semi-automated solution uses Python scripts to generate the GTFS feed, which transit agencies can easily customize and maintain. The feed generated from our work is operational. In an effort to promote GTFS adoption, particularly in resource-constrained countries, we are making our code publicly available. This can significantly improve access to public transit information for citizens.

## Statement of Need
In recent years, Islamabad, the capital of Pakistan, has seen substantial improvements in its public transport infrastructure, marked by the addition of the Red, Green, Blue, and Orange metro bus lines, as well as the introduction of an electric vehicle (EV) service.However, an important challenge thats remains unnoticed is the lack of accessible digital transit information for daily commuters. To overcome this challenge implemented GTFS for the Orange Metro Bus and developed a python scripts that is semiautomated which helps to make standardize transit feeds in easy and faster way. In many developing countries, the lack of digitalized schedules and route data in public transportation systems makes it difficult for commuters to plan their trips. This study tackles this issue by leveraging semi-automated Python scripts to generate GTFS feeds, bridging the gap between raw data collection and integration with trip-planning tools like Google Maps — a methodology similarly explored in the Digital Matatu Project for Nairobi's semi-formal transit system [@williams2015digital]. By simplifying the process of creating standardized transit feeds, our approach supports smart city initiatives and enhances urban mobility, aligning with the broader goals of GTFS adoption in resource-constrained contexts [@eros2014gtfs].

## Methodology
This section explains how the GTFS data for the Orange Line Metro Bus in Islamabad was developed and implemented. It covers the process of collecting relevant data, organizing it into GTFS format, and using Python scripts to automate different steps.

### **Data Collection**

One of the key components of our data was the stop coordinates and bus schedules for the Orange Line Metro. While the main station locations and timings were provided by the transit authority, the official data was incomplete. To fill the gaps, we manually collected additional entry and exit point coordinates from Google Maps. This helped us build a more accurate and complete dataset, with precise latitude and longitude values for each station, making it reliable for analysis and mapping.

### **GTFS Components**

While preparing the GTFS dataset, created several standard text files to define different parts of the transit system following the GTFS specification [@gtfs_reference]. The *agency.txt* file includes basic details about the transport authority, like its name, website,time zone and also requires an id to assign an id to the agency. Route-level data is stored in routes.txt, which lists each route along with its name, ID, type (such as metro or bus), and the agency it belongs to. The **trips.txt** file links these routes to individual trips, while "stop\_times.txt" provides the actual schedule, showing when each trip stops at each station ,like when a bus arrive at stops and when it departure. We used **stops.txt"** to record all stop locations, including their names and precise coordinates. The **calendar.txt** file defines which days the services run like weekdays, weekends, or specific dates. The **fare\_attributes.txt** holds the fare rules, such as ticket prices, payment types, and transfer policies and finally **fare\_rules.txt** provide the links of fare with routes if different routes has different fares. Together, these files form a complete GTFS feed that helps organize, map, and plan the transit service more effectively.**Figure 1**  illustrates the GTFS schema, showing the relationship between stops, routes, trips, and 

![GTFS schema showing relationships between stops, routes, trips, and schedules.](https://raw.githubusercontent.com/Mavi2902/GTFS-Automation/main/paper/images/GTFS.jpg)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Figure 1: GTFS schema showing relationships between stops, routes, trips, and schedules.**



schedules. Hence, also shows the linking of different files like stops, routes, trips, schedules, etc.

### **Automation Using Python**
Certain GTFS files, such as trips.txt and stop\_times.txt,require large and complex datasets. However, the majority of GTFS files are quite simple and easily created manually. To address this, we suggest automating their creation with two scripts. Here is the pseudo-code of these scripts which creates the stop_times.txt and trips.txt files.

#### **Script 1: Generating stop_times.txt**

To generate stop_times.txt in the GTFS feed automatically, we suggest the following approach. This script automates the assignment of stop sequences, arrival times, and departure times, minimizing manual effort and ensuring efficient scheduling.
```text
 INITIALIZE:
    INPUT start_time (HH:MM:SS)
    INPUT last_trip_time (HH:MM:SS)
    INPUT num_stops (≥ 2)
    INPUT dwell_time_seconds (≥ 0)
    INPUT gap_time_minutes (≥ 0)
    INPUT starting_trip_id (must end with digits)
    FOR each stop FROM 1 TO num_stops:
        INPUT stop_id
    FOR each segment FROM 1 TO num_stops–1:
        INPUT travel_time_seconds BETWEEN stop_i and stop_i+1 (≥ 1)

VALIDATE all inputs

SET current_trip_id = starting_trip_id
SET current_time = start_time
CREATE empty list stop_times

WHILE current_time ≤ last_trip_time DO:
    SET cumulative = 0
    FOR stop_sequence FROM 1 TO num_stops:
        CALCULATE arrival = current_time + cumulative
        CALCULATE departure = arrival + dwell_time_seconds
        APPEND [current_trip_id, arrival, departure, stop_id, stop_sequence] TO stop_times
        IF stop_sequence < num_stops THEN:
            cumulative += travel_time_seconds[stop_sequence] + dwell_time_seconds
        END IF
    END FOR

    CALL increment_trip_id(current_trip_id)
    INCREMENT current_time BY gap_time_minutes

END WHILE

OPEN "stop_times.txt"
WRITE header: trip_id,arrival_time,departure_time,stop_id,stop_sequence
FOR each record IN stop_times:
    WRITE record AS CSV row
END FOR

PRINT "stop_times.txt file successfully created"
```


#### **Script 2: Generating trips.txt**

The following algorithm is designed to generate trips.txt in the GTFS feed automatically. This script systematically creates trip identifiers, assigns route and service details, and structures the dataset for integration into public transportation systems.

```text
INPUT number_of_routes

FOR each route FROM 1 TO number_of_routes:
    PROMPT user to enter:
        - route_id (e.g., r-OLI-1)
        - service_id (e.g., WD)
        - first_trip_id (e.g., t-OLI-1-001)
        - headsigns (e.g., Stop A to Stop Z, Stop Z to Stop A)
        - number_of_trips for each headsign (e.g., 15, 15)
        - block_ids (optional; e.g., B1, B2)
        - shape_ids (optional; e.g., SHP1, SHP2)

    CLEAN optional inputs by removing blanks

    EXTRACT numeric part and base from first_trip_id

    FOR each headsign (indexed by i):
        FOR trip_num FROM 0 TO number_of_trips[i] - 1:
            CREATE new trip_id by incrementing the base numeric part
            BUILD trip entry with:
                - trip_id
                - route_id
                - service_id
                - standardized headsign
                - direction_id = i
                - block_id (if given)
                - shape_id (if given)
            ADD trip entry to trips_data

    APPEND all trips_data for this route to overall_trips_list

IF overall_trips_list is not empty:
    OPEN `trips.txt` for writing
    WRITE header: route_id, service_id, trip_id, trip_headsign, direction_id, block_id, shape_id
    FOR each trip in list:
        WRITE trip as CSV row

PRINT "trips.txt generated successfully"
```






Automating the creation of trips.txt and stop_times.txt makes it much easier to build and manage a GTFS feed. With this approach, transit agencies can create properly structured transit data without needing deep technical skills. It also cuts down on manual work, making it more feasible for cities with limited time or resources to adopt GTFS and digitize their transit schedules.

## Validation

To ensure the correctness and reliability of the generated GTFS feed, we conducted a comprehensive validation process using both automated tools and real-world integration. The validation focused on structural integrity, error detection, and successful deployment in transit applications.

### **GTFS Feed Generation and Validation**

In our semi-automated approach, only stop\_times.txt and trips.txt were generated using automation, as these files require complex calculations related to trip scheduling and stop timings. The remaining GTFS files  such as agency.txt,calendar.txt, stops.txt, routes.txt etc were created manually since they contain mostly static information that doesn't change frequently.
To ensure the GTFS feed met required standards, we validated the entire dataset using official GTFS Validator[@mobilitydata_validator]. This tool checks for structural accuracy and compliance with the GTFS specification.The validation process included the following steps:

- **Schema Validation**: Confirmed that all GTFS files, both manually and automatically generated  were properly formatted and correctly linked (agency.txt, trips.txt, stops.txt, stop\_times.txt, routes.txt, calendar.txt, etc.).
- **Error Detection**: The validator initially flagged minor formatting issues, such as missing stop times and incorrect route references. These errors were identified and manually corrected before final deployment.
- **Completeness Check**: Verified that every transit stop had associated route and schedule entries, ensuring full integration with trip-planning tools.

After addressing these issues, the GTFS feed successfully passed all validation checks, confirming that it was accurate, complete, and ready for real-world deployment.


### **Integration with Google Transit**

The GTFS feed was uploaded to the Google Transit Data Feed portal after validation.Once processed by Google, the transit schedules and routes became available on Google Maps, allowing users to plan trips using real-time public transit data [@google_transit]. This confirmed that the GTFS feed functioned correctly in a real-world scenario.

### **GTFS Implementation for the Orange Line Metro Bus** 
To validate the real-world application of the generated GTFS feed, we deployed it for the Islamabad Orange Line Metro Bus. Below are samples from the automated GTFS files (stop_times.txt and trips.txt) generated using our Python scripts.

#### **Sample from stop_times.txt**

This file records arrival and departure times for each stop along a route: trip_id,arrival_time,departure_time,stop_id,stop_sequence,timepoint t-OLI-1-001,6:00:00,6:00:15,s-OLI-1-001,1,1 t-OLI-1-001,6:02:27,6:02:42,s-OLI-1-002,2,1 t-OLI-1-001,6:05:10,6:05:25,s-OLI-1-003,3,1

#### **Sample from trips.txt**

This file defines trips with route and service details: trip_id,route_id,service_id,trip_headsign t-OLI-1-001,r-OLI-1,r-OLI-1_Weekdays,Faf to N5 t-OLI-1-002,r-OLI-1,r-OLI-1_Weekdays,Faf to N5 t-OLI-1-003,r-OLI-1,r-OLI-1_Weekdays,Faf to N5

Once processed by Google Transit, the generated GTFS feed was successfully integrated into Google Maps, making it publicly accessible for commuters. **Figure 2** shows the live Orange Line Metro schedule appearing in Google Maps, confirming successful deployment.The validation process demonstrated that our semi-automated approach effectively produces accurate, structured, and reliable GTFS feeds while allowing transit agencies to input small static data where automation is unnecessary manually.

![Figure 2: GTFS feed successfully integrated into Google Maps](https://raw.githubusercontent.com/Mavi2902/GTFS-Automation/main/paper/images/Orange%20line%20google%20map%20visualization.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Figure 2:** GTFS feed successfully integrated into Google Maps, displaying Orange Line Metro transit data.





## Conclusion

This study presents a practical and semi-automated approach for generating GTFS feeds, demonstrated through the case of Islamabad's Orange Line Metro Bus. By automating the creation of complex files like **trips.txt** and **stop\_times.txt**, our method significantly reduces manual effort and potential errors. The approach is designed to be accessible for transit authorities with limited technical expertise, enabling them to digitize and publish transit data efficiently. The successful integration of the generated GTFS feed with Google Maps confirms its accuracy and reliability. Overall, this work supports broader GTFS adoption in developing regions and contributes to the goal of improving public access to structured transit information.


## Future Work

While our current work automates the generation of two key GTFS files (stop_times.txt and trips.txt), future developments will aim to automate additional GTFS components such as stops.txt, routes.txt, and calendar.txt. Integrating real-time transit data to provide live updates and vehicle tracking represents another important direction.
Moreover, the current code can be generalized for implementation in other cities, facilitating a scalable framework adaptable to various transit authorities. In the future, we also plan to develop simple and user-friendly interfaces so that even non-technical users can easily create and manage GTFS feeds. This will make the process more accessible and encourage community involvement through open data sharing and collaborative improvements.

## Software Availability

The GTFS automation scripts and dataset for Islamabad's Orange Line Metro Bus are publicly available at [GitHub repository code  folder](https://github.com/Mavi2902/GTFS-Automation/tree/main/code). This software is released under the MIT License.

## Acknowledgments

This work was conducted under the project GCF-744: "Optimum Use of Existing Resources– A Prototype Model of Road Safety," funded by the Higher Education Commission (HEC) of Pakistan. We acknowledge the Transit Authority of Islamabad CDA (Capital Development Authority) for their collaboration and for providing access to transit data, which was instrumental in developing and validating the GTFS automation system.

## Reference
