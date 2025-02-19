Risky Symbol Identification

Overview

This repository contains Python scripts to identify risky trading symbols based on trade data. The scripts fetch data from a database or an uploaded CSV file, analyze trading activity, and generate risk reports. These tools help in monitoring and assessing high-risk trading patterns over different timeframes.

Files

1. 24 hours.py

Fetches trade data from a MySQL database within a user-specified time range (e.g., last 24 hours or any custom range).

Classifies symbols into different asset classes (Forex, Crypto, Indices, Commodities) for better analysis.

Fetches associated account and customer details for deeper insights.

Saves the extracted data with asset classifications into trades_with_asset_classes.csv.

2. symbol wise risk report.py

Loads trade data from a user-uploaded CSV file.

Filters trades belonging to real accounts.

Groups data by trading symbols and calculates key metrics:

Total number of trades per symbol

Total traded lots per symbol

Total profit and loss (PnL)

Number of unique traders per symbol

Separates positive-profit trades and calculates profitable trade metrics.

Generates a final risk report and saves it as SymbolWise.csv.

Requirements

Python 3.x

Required Python Libraries:

pandas

sqlalchemy

mysql-connector-python

tkinter

openpyxl

Installation

Clone this repository:

git clone https://github.com/yourusername/Risky-Symbol-Identification.git
cd Risky-Symbol-Identification

Install dependencies:

pip install pandas sqlalchemy mysql-connector-python openpyxl

Usage

Running the Scripts

Execute 24 hours.py

Modify start_time and end_time to set your desired time range.

Ensure correct database credentials are configured.

Run the script:

python "24 hours.py"

The output file trades_with_asset_classes.csv will be generated.

Execute symbol wise risk report.py

Run the script:

python "symbol wise risk report.py"

Select the CSV file containing trade data when prompted.

The script will process and generate a report saved as SymbolWise.csv.

Output Files

trades_with_asset_classes.csv:

Contains extracted trade data along with classified asset classes.

SymbolWise.csv:

Summarized report of risky symbols based on trading activity.

Includes trader count and profitability metrics.

Notes

Ensure you have the correct database credentials before executing 24 hours.py.

symbol wise risk report.py requires an input CSV file.

Modify SQL queries and filters if your database structure differs from the expected format.
