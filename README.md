# Real-Time Ride Booking Data Engineering Project

## Project Overview

This project is an **end-to-end Azure Data Engineering solution** that simulates a real-world **ride-booking platform similar to Uber**.

The project processes both **real-time ride-booking events** and **batch data**, using Azure services and Databricks to build a complete data pipeline from **data ingestion to analytical data modeling**.

The solution demonstrates how modern data engineering technologies can be integrated to build a scalable pipeline capable of handling:

- Real-time streaming data
- Batch data ingestion
- Data transformation and cleansing
- Incremental data processing
- Metadata-driven pipelines
- Slowly Changing Dimensions (SCD)
- Medallion Architecture
- Star Schema data modeling
- Analytical-ready datasets

---

## Project Architecture

```text
                         ┌──────────────────────┐
                         │   Ride Booking       │
                         │    Web Application   │
                         └──────────┬───────────┘
                                    │
                                    │ Real-Time Events
                                    ▼
                         ┌──────────────────────┐
                         │   Azure Event Hubs   │
                         │   Streaming Ingestion│
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Azure Databricks     │
                         │ PySpark Streaming    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Bronze Layer         │
                         │ Raw Streaming Data   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Silver Layer         │
                         │ Cleaned & Transformed│
                         │ Data                 │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Gold Layer           │
                         │ Business-Ready Data  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     Star Schema      │
                         │ Fact & Dimensions    │
                         └──────────────────────┘


     Batch Data Sources
             │
             ▼
┌──────────────────────────┐
│ Azure Data Factory (ADF) │
│ Dynamic Ingestion        │
│ Lookup + ForEach         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Azure Data Lake Storage  │
│          Gen2            │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      Databricks          │
│ Batch + Streaming        │
│ Processing               │
└──────────────────────────┘


```
### Pipeline Run Output

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/5b5a605d-4e82-4b46-9b1d-ea11ee281003"
    alt="Pipeline Run Output"
    width="90%"
  />
</p>

### Pipeline Performance

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/6a56205d-e2be-4035-a3fd-de90577b651e"
    alt="Pipeline Performance"
    width="90%"
  />
</p>
