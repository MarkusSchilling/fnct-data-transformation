import os
import pandas as pd
from Module import fnct_calculations as calcs
from Module import write_two_header_csv as csvhead

def secondary_data_read_in(file_path, secondary_data_folder, primary_data_folder):
    xls = pd.ExcelFile(file_path)

    # Specify the name of the secondary data CSV file (to be created, if not already existing)
    secondary_data_file = "FNCT_secondary_data.csv"
    # Path to existing secondary data CSV file
    secondary_data_file_path = os.path.join(secondary_data_folder, secondary_data_file)

    # Define column headers, note that there are two header lines
    first_header = ['Specimen_ID', 'Process_ID', 'Material', 'Width w', 'Thickness t', 'Notch depth nominal nn', 'Residual fracture surface nominal An', 'Stress nominal sigma_n', 'Measurement Station', 'Medium', 'Force', 'Start of measurement', 'End of measurement', 'Time to failure tf', 'Final elongation d', 'Residual fracture surface measured AL1', 'Residual fracture surface measured AL2', 'Residual fracture surface measured AL', 'Notch depth measured nm', 'Stress measured sigma_L', 'Test temperature', 'Conditioning time', 'Leverage ratio', 'Primary Data Path']
    second_header = ['', '', '', 'mm', 'mm', 'mm', 'mm²', 'MPa', '', '', 'N', '', '', 'h', 'mm', 'mm²', 'mm²', 'mm²', 'mm', 'MPa', '°C', 'h', '', '']

    # Check if the secondary data CSV file exists
    if os.path.exists(secondary_data_file_path):
        # Load existing secondary data into DataFrame
        try:
            existing_secondary_data = pd.read_csv(secondary_data_file_path, sep=';', dtype=str, header=[0, 1], encoding='ISO-8859-1')
        except UnicodeDecodeError:
            existing_secondary_data = pd.read_csv(secondary_data_file_path, sep=';', dtype=str, header=[0, 1], encoding='utf-8')
    else:
        # If the file doesn't exist, create an empty DataFrame with respective column names
        existing_secondary_data = pd.DataFrame(columns=pd.MultiIndex.from_tuples(zip(first_header, second_header)))
        csvhead.save_csv_with_two_headers(existing_secondary_data, secondary_data_file_path, first_header, second_header)
        print(f"No existing secondary data found at {secondary_data_file_path}. Creating new FNCT_secondary_data.csv file.")

    # Initialize an empty list to hold new secondary data
    new_secondary_data = []

    # Calculate value of final elongation by using the corresponding function
    final_elongation_value = calcs.get_calculation_final_elongation(xls)

    # Read and transform data from each new Excel file
    if 'Daten' in xls.sheet_names:
        daten_df = pd.read_excel(xls, 'Daten')

        # Iterate over each row in daten_df to check and append new data
        for index, row in daten_df.iterrows():
            process_id = daten_df.iloc[0, 22]

            # Check if the Process_ID already exists in existing_secondary_data
            if process_id not in existing_secondary_data['Process_ID'].values:
                # Perform transformations on daten_df as needed to match the existing format
                new_data_included = [
                    '', # Specimen_ID: needs to be assigned manually after data transformation
                    daten_df.iloc[0, 22], # Process_ID
                    '', # Material: needs to be assigned manually after data transformation
                    daten_df.iloc[0, 45], # Width w
                    daten_df.iloc[0, 46], # Thickness t
                    daten_df.iloc[0, 47], # Notch depth nominal
                    calcs.get_calculation_nominal_fracture_surface(daten_df), # nominal residual fracture surface
                    daten_df.iloc[0, 48], # Stress nominal sigma_n
                    daten_df.iloc[0, 26], # Measurement Station
                    '', # Medium: needs to be assigned manually after data transformation
                    daten_df.iloc[0, 33], # Force
                    daten_df.iloc[0, 52], # Start of Measurement
                    daten_df.iloc[0, 53], # End of Measurement
                    daten_df.iloc[0, 55], # Time to failure tf
                    final_elongation_value, # Final elongation d
                    '', # Residual fracture surface measured AL1: Obtained in separate analysis process (different measurement process), needs to be assigned manually
                    '', # Residual fracture surface measured AL2: Obtained in separate analysis process (different measurement process), needs to be assigned manually
                    '', # Residual fracture surface measured AL: Obtained in separate analysis process (different measurement process), needs to be assigned manually
                    '', # Notch depth measured nm: Obtained in separate analysis process (different measurement process), needs to be assigned manually
                    '', # Stress measured sigma_L: Obtained in separate analysis process (different measurement process), needs to be assigned manually
                    daten_df.iloc[0, 27], # Test temperature
                    daten_df.iloc[0, 28], # Conditioning time
                    1, # Leverage ratio
                    os.path.join(primary_data_folder, daten_df.iloc[0, 22] + ".csv") # Path to primary data 
                ]
                # Append the new row to the new_secondary_data list
                new_secondary_data.append(new_data_included)

    # Convert new_secondary_data to a DataFrame if it is not already
    if len(new_secondary_data) > 0:
        new_secondary_data = pd.DataFrame(new_secondary_data, columns=existing_secondary_data.columns)
    else:
        new_secondary_data = pd.DataFrame(columns=existing_secondary_data.columns)

    # Avoid NA and NaN entries and fill with an empty string
    existing_secondary_data = existing_secondary_data.fillna('')
    new_secondary_data = new_secondary_data.fillna('')

    # Combine existing secondary data with new secondary data
    combined_secondary_data = pd.concat([existing_secondary_data, new_secondary_data], ignore_index=True)

    # Save the combined secondary data back to the secondary_data CSV file using the specifically defined two header write CSV function
    csvhead.save_csv_with_two_headers(combined_secondary_data, secondary_data_file_path, first_header, second_header)
