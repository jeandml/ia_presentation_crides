import pandas as pd
import os
import zipfile

def process_zip_files(folder_path, keyword, output_file):
    compiled_data = pd.DataFrame()

    for file in os.listdir(folder_path):
        if file.endswith('.zip'):
            zip_path = os.path.join(folder_path, file)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
                csv_file = zip_ref.namelist()[0]  # Assuming each zip contains only one csv
                csv_path = os.path.join(folder_path, csv_file)

                chunk_size = 10000  # Adjust based on memory capacity
                for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
                    filtered_data = chunk[chunk.apply(lambda row: row.astype(str).str.contains(keyword).any(), axis=1)]
                    compiled_data = pd.concat([compiled_data, filtered_data])

                os.remove(csv_path)  # Remove extracted file to save space

    compiled_data.to_csv(output_file, index=False)

folder_path = input("Enter the folder path where zip files are stored: ")
keyword = 'misinformation'
output_file = 'filtered_data.csv'

process_zip_files(folder_path, keyword, output_file)
