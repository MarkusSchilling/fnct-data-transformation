# This method allows to read in metadata of FNCT data. 
# It has to be noted, that some metadata information is stored statically, such as the institution and its address (see in code lines below). 

import os 
import pandas as pd

def metadata_read_in(file_path, metadata_folder):
    xls = pd.ExcelFile(file_path)

    # Read the tab "Daten" if it exists
    if 'Daten' in xls.sheet_names:
        daten_df = pd.read_excel(xls, 'Daten')
    else:
        print(f"Skipping {file_path} for metadata consideration, because 'Daten' tab not found")
        return

    # Get the CSV file name from the second line of column "W"
    csv_file_name = daten_df.iloc[0, 22] + '_metadata.csv'

    # Specify the headers
    headers = [
        ('Standard', ''),
        ('Laboratory', ''),
        ('Institute', ''),
        ('Address', ''),
        ('Location', ''),
        ('Load Cell Maximum Force', 'N'),
        ('Test machine name', ''),
        ('Test machine serial number', ''),
        ('Test machine manufacturer', ''),
        ('Test machine manufacturer Location', ''),
        ('Funding Party', ''),
        ('Funding Party ID', ''),
        ('Grant number', ''),
        ('Preload', 'N'),
        ('Preload time', 's'),
        ('Test Force increase rate', 'N/s'),
        ('Limit Test Movement', 'mm')
        ]
    
    # Reorganize the data as needed for metadata and store it to the new dataframe
    metadata_df = pd.DataFrame({
        'ColumnA': 'ISO 16770:2019',
        'ColumnB': '',
        'ColumnC': '',
        'ColumnD': '',
        'ColumnE': '',
        'ColumnF': [200],
        'ColumnG': '',
        'ColumnH': '',
        'ColumnI': '',
        'ColumnJ': '',
        'ColumnK': '',
        'ColumnL': '',
        'ColumnM': '',
        'ColumnN': daten_df.iloc[0, 39],
        'ColumnO': daten_df.iloc[0, 40],
        'ColumnP': daten_df.iloc[0, 41],
        'ColumnQ': daten_df.iloc[0, 42]
    })

    # Set the new headers to the dataframe
    metadata_df.columns = pd.MultiIndex.from_tuples(headers)

    # Save the dataframe to a new CSV file, but skip the file creation if a file with the same name already exists to avoid unintended overwriting
    csv_file_path = os.path.join(metadata_folder, csv_file_name)
    if os.path.exists(csv_file_path):
        print(f"Skipping {csv_file_name}, as the associated CSV file '{csv_file_name}' already exists.")
    else:
        # Save the transformed data to a new CSV file in "primary_data" folder
        metadata_df.to_csv(csv_file_path, index=False, sep=';')