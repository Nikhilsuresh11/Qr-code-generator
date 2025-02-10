```mermaid
graph RL;
    N[Google Looker Studio] -->|Dashboards & Reports| M[Visualization];
    M -->|Final Processed Data| L[dbt];
    L -->|ETL & Aggregation| K[Data Modeling];
    K -->|Transforms Data| J[Snowflake];

    G[Storage & Analytics] -->|Advanced Analytics| J[Snowflake];
    G -->|Raw Backup| I[Cloud Storage];
    G -->|Fast Queries| H[BigQuery];

    F[Dataflow] -->|Cleaned Data| G[Storage & Analytics];
    D[Data Processing] -->|Batch Processing| F;
    D -->|Real-time Processing| E[Cloud Functions];
    C[Google Pub/Sub] -->|Streaming Data| D[Data Processing];
    B -->|MQTT/HTTP| C[Google Pub/Sub];
    A[IoT Device] -->|Data Collection| B[Data Ingestion];



```






















---

# QR Code Generator using Streamlit

## Overview

This project is a simple QR code generator built using Streamlit, a popular Python library for creating web apps with minimal effort. With this tool, users can easily generate QR codes for various purposes such as sharing links, contact information, or any other text-based data.

![QR Code Generator Demo](demo.gif)

## Features

- Generate QR codes for text-based data.
- Customize QR code size and color.
- Download generated QR codes as image files.

## Installation

To use this QR code generator, follow these steps:

1. Clone this repository to your local machine:

   ```
   https://github.com/Nikhilsuresh11/Qr-code-generator.git
   ```

2. Navigate to the project directory:

   ```
   cd qr-code-generator
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

To run the QR code generator app, execute the following command:

```
streamlit run QR.py
```

Once the Streamlit server is running, open your web browser and navigate to the provided URL (usually `http://localhost:8501`). You will see the QR code generator interface where you can input your data and customize the QR code as needed.
