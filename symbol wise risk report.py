import pandas as pd
from tkinter import Tk, filedialog

# Function to upload the file
def upload_file():
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    root.destroy()
    return file_path

# Upload the file and load the dataset
file_path = upload_file()
if file_path:
    try:
        df = pd.read_csv(file_path)

        # Filter the data for Real accounts based on the type_account column
        real_accounts_df = df[df['type_account'].str.contains('real', case=False, na=False)]

        # Group by the 'symbol' column and calculate the metrics for all PnL (profits and losses), and unique trader count
        summary_df_with_pnl = real_accounts_df.groupby('symbol').agg(
            trade_count=('symbol', 'size'),
            total_lots=('FinalLot', 'sum'),
            total_pnl=('profit', 'sum'),
            trader_count=('login', 'nunique')  # Count of unique logins per symbol
        ).reset_index()

        # Filter the data for positive profits and group again
        positive_profits_df = real_accounts_df[real_accounts_df['profit'] > 0].groupby('symbol').agg(
            trade_count=('symbol', 'size'),
            total_lots=('FinalLot', 'sum'),
            Profit=('profit', 'sum')  # Renaming 'profit' to 'Profit'
        ).reset_index()

        # Merge the total pnl (including losses) with the positive profits data
        final_df = pd.merge(summary_df_with_pnl, positive_profits_df[['symbol', 'Profit']], on='symbol', how='left')

        # Save the result to a CSV file named "SymbolWise.csv"
        output_path = "SymbolWise.csv"
        final_df.to_csv(output_path, index=False)
        print(f"File saved successfully as {output_path}")

    except FileNotFoundError:
        print("The file path entered is not valid. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}") 
else:
    print("No file selected.")