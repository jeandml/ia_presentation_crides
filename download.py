import requests
from datetime import datetime, timedelta

#Define function to download files based on start_date and end_date
def download_files(start_date, end_date):
    base_url = "https://dsa-sor-data-dumps.s3.eu-central-1.amazonaws.com/sor-global-"
    date_format = "%Y-%m-%d"

    # Convert string dates to datetime objects
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    current_date = start

    while current_date <= end:
        # Format the date and create the download URL
        date_str = current_date.strftime(date_format)
        download_url = f"{base_url}{date_str}-full.csv.zip"

        # Download the file
        response = requests.get(download_url)
        if response.status_code == 200:
            with open(f"sor-global-{date_str}-full.csv.zip", 'wb') as f:
                f.write(response.content)
            print(f"Downloaded file for {date_str}")
        else:
            print(f"Failed to download file for {date_str}")

        # Move to the next day
        current_date += timedelta(days=1)

# Ask the user for input
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Run the download function with user input
download_files(start_date, end_date)
