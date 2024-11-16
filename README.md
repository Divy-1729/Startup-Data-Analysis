# Startup Data Analysis and Visualization Tool

## Overview
This project is designed to analyze and visualize data from a CSV file named `Unicorn_Clean.csv`, which contains records of **935 startups worldwide**. The dataset includes information such as:
- **Company Valuation ($B)**
- **Date Joined**
- **Country**
- **City**
- **Industry**
- **Investor Details**

## Key Features

### 1. Data Display
- Reads and displays startup data from the `Unicorn_Clean.csv` file.
- Uses the **pandas** library for efficient data handling and manipulation.

### 2. User Interaction
- Features a user-friendly **Graphical User Interface (GUI)** built with the **tkinter** library.
- Offers menu-driven operations, including:
  - Viewing the dataset
  - Searching for specific records
  - Visualizing data with charts

### 3. Data Modification
- Interactive GUI for updating and modifying dataset records.
- Includes **Entry widgets** and buttons to edit fields such as:
  - Index
  - Company Name
  - Valuation
  - Other attributes

### 4. Data Visualization
- Generates visual insights using the **matplotlib** library.
- Provides options to create:
  - **Bar Charts**
  - **Line Charts**
  - **Histograms**

### 5. Search Functionality
- Search for specific data points based on user-defined criteria.
- Displays detailed results in the GUI for easy reference.

## Development Environment

- **Programming Language**: Python
- **Integrated Development Environment (IDE)**: PyCharm

## Data Source
The `Unicorn_Clean.csv` dataset is sourced from [Kaggle](https://www.kaggle.com), featuring data on 935 startups globally.
