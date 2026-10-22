# yuvaintern-logistics-data-analyst-week1
# 📦 Logistics Data Analyst Internship - Week 1: Strategic Planning & Data Exploration

**Intern Name:** Aastha Jain  
**Organization:** YuvaIntern (in collaboration with Henry Harvin & NSDC)  
**Project Focus:** Logistics Supply Chain Optimization & Predictive Analytics Framework  

---

## 🚀 Project Overview
This repository contains the deliverables for **Week 1** of the Logistics Data Analyst Internship. The project establishes a comprehensive strategic planning and data exploration framework designed to optimize last-mile delivery, reduce operational overhead, and improve supply chain efficiency for **"SwiftExpress Logistics,"** a regional 3PL delivery network.

---

## 🎯 Key Objectives & Scenario
* **Scenario:** Managing urban and semi-urban parcel deliveries across Madhya Pradesh during peak festive seasons, mitigating transit delays, and improving estimated time of arrival (ETA) accuracy.
* **Core Challenges:** Unoptimized routing, unexpected en-route transit delays, and warehouse dispatch bottlenecks.

---

## 📊 Key Performance Indicators (KPIs)
| KPI Name | Target Metric | Business Objective |
| :--- | :--- | :--- |
| **On-Time Delivery Rate (OTDR)** | > 95% | Ensure parcels reach customers within the committed delivery window. |
| **Average Transit Delay** | < 45 mins / order | Minimize unexpected delays caused by traffic or sub-optimal routing. |
| **Cost per Delivery (CPD)** | 10-15% reduction | Optimize fuel usage and vehicle capacity utilization. |

---

## 🔬 Data Science Methodologies
1. **Regression Analysis:** Forecasting delivery times and delay durations using features like distance, traffic density, and weather conditions.
2. **K-Means Clustering:** Grouping delivery locations and regional hubs to decentralize inventory and streamline dispatch zones.
3. **Optimization Algorithms:** Applying Vehicle Routing Problem (VRP) heuristics for efficient route sequencing.

---

## 🗺️ Strategic Roadmap
1. **Data Collection:** Ingesting historical delivery logs, GPS telematics, and warehouse timestamps.
2. **Data Cleaning:** Handling missing timestamps, dropping duplicates, and normalizing coordinates.
3. **Exploratory Data Analysis (EDA):** Visualizing delay distributions using Pandas, Matplotlib, and Seaborn.
4. **Predictive Modeling & Reporting:** Training ML models and constructing Power BI dashboards.

---

## 💻 Python Script (`logistics_analysis.py`)
The repository includes a clean Python preprocessing script (`logistics_analysis.py`) that handles missing values, engineers transit time features, and computes vital logistics KPIs.

### How to Run the Script:
```bash
python logistics_analysis.py
