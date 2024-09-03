import os 
import pandas as pd

def primary_data_read_in(file_path, primary_data_folder):
    xls = pd.ExcelFile(file_path)

    # Read the tab "Daten" if it exists
    if 'Daten' in xls.sheet_names:
        daten_df = pd.read_excel(xls, 'Daten')
    else:
        print(f"Skipping {file_path} for primary data consideration, because 'Daten' tab not found")
        return

    # Get the CSV file name from the second line of column "W" (column number 22 in dataframe)
    csv_file_name = daten_df.iloc[0, 22] + '.csv'

    # Read the tab "Daten_record", skipping the first line and taking the first 4 columns
    if 'Daten_record' in xls.sheet_names:
        daten_record_df = pd.read_excel(xls, 'Daten_record', skiprows=1, usecols='A:D')

        # Specify the new headers
        new_headers = [
            ('Duration', 'h'),
            ('Force', 'N'),
            ('Elongation', 'mm'),
            ('Temperature', '°C')
        ]

        # Set the new headers to the dataframe
        daten_record_df.columns = pd.MultiIndex.from_tuples(new_headers)

        # Save the dataframe to a new CSV file, but skip the file creation if a file with the same name already exists to avoid unintended overwriting
        csv_file_path = os.path.join(primary_data_folder, csv_file_name)
        if os.path.exists(csv_file_path):
            print(f"Skipping {csv_file_name}, as the associated CSV file '{csv_file_name}' already exists.")
        else:
            # Save the transformed data to a new CSV file in "primary_data" folder
            daten_record_df.to_csv(csv_file_path, index=False, sep=';')
    else:
        print(f"Skipping {file_path} - 'Daten_record' tab not found")
        return 