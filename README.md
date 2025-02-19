Risky-Symbol-Identification

Overview

This repository, Risky-Symbol-Identification, contains Python scripts to analyze trading data, identify risky trading symbols, and generate summary reports. The scripts fetch trade data from a database, process the data, and generate insights into trading risks based on symbols.

Scripts

1. 24_hours.py

This script fetches trade data for a specified time range (default: last 24 hours, but can be modified) from a MySQL database. It categorizes trades based on asset classes and enriches the data with account and customer details before saving it to a CSV file.

Features:

Connects to a MySQL database using SQLAlchemy.

Retrieves trade data within a specified time range.

Categorizes assets into Crypto, Commodities, Indices, and Forex.

Merges trade data with account and customer information.

Outputs a CSV file (trades_with_asset_classes.csv) with detailed trade information.

Usage:

Modify the start_time and end_time variables to fetch data for a different time range.

2. symbol_wise_risk_report.py

This script processes the trade data CSV file generated by 24_hours.py and creates a summary of risky symbols. It identifies trades with positive and negative PnL and calculates trade count, lot sizes, and unique trader count per symbol.

Features:

Allows file selection via a file upload dialog.

Filters data for real trading accounts.

Groups trades by symbol and calculates:

Total number of trades.

Total lots traded.

Total PnL (profits and losses combined).

Count of unique traders.

Separately analyzes symbols with only positive PnL.

Merges both datasets to get a consolidated risk report.

Saves the summary report as SymbolWise.csv.

Usage:

Run the script, select the CSV file generated by 24_hours.py, and it will process the data to create the risk summary.

Weekly Risk Report Generation

Using symbol_wise_risk_report.py, a weekly risk report can be created by:

Running 24_hours.py daily or for the past week’s data range.

Running symbol_wise_risk_report.py on the weekly dataset.

Aggregating the results to identify consistently risky symbols.
