import pandas as pd

def convert_to_float(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return None
        
def get_calculation_nominal_fracture_surface(daten_df):
    residual_fracture_surface_nominal = (daten_df.iloc[0, 45]-2*daten_df.iloc[0, 47])*(daten_df.iloc[0, 46]-2*daten_df.iloc[0, 47])
    return residual_fracture_surface_nominal

def find_corresponding_value(df, search_column_name, search_value, extract_column_name):
    # Find the index of the last value in search_column that is greater than the search_value
    filtered_df = df[df[search_column_name] > search_value]
    last_higher_index = filtered_df.index[-1] if not filtered_df.empty else None
     
    # Extract the corresponding value from extract_column
    corresponding_value = df.loc[last_higher_index, extract_column_name]
    return corresponding_value

def get_calculation_final_elongation(xls):
    if 'Daten' in xls.sheet_names:
        cell_value_df = pd.read_excel(xls, 'Daten')
        search_value = cell_value_df.iloc[0, 33]/2
    
    if 'Daten_record' in xls.sheet_names:
        daten_record_df = pd.read_excel(xls, 'Daten_record', skiprows=0, usecols='B:C')

    # Define the search and extract columns (using iloc)
    search_column = daten_record_df.iloc[:, 0]
    extract_column = daten_record_df.iloc[:, 1]

    # Convert the series to DataFrame columns for proper filtering
    search_column_name = search_column.name
    extract_column_name = extract_column.name

    final_elongation = find_corresponding_value(daten_record_df, search_column_name, search_value, extract_column_name)
    return final_elongation

def get_calculation_residual_fracture_surface_measured(AL1, AL2):
    # Convert AL1 and AL2 to float, handle non-numeric values
    AL1 = convert_to_float(AL1)
    AL2 = convert_to_float(AL2)

    if AL1 is None and AL2 is None:
        total_sum = 0
        count = 1
    elif AL1 is None:
        total_sum = AL2
        count = 1
    elif AL2 is None:
        total_sum = AL1
        count = 1
    elif AL1 == 0 and AL2 == 0:
        total_sum = 0
        count = 1
    elif AL1 == 0:
        total_sum = AL2
        count = 1
    elif AL2 == 0:
        total_sum = AL1
        count = 1
    else:
        total_sum = AL1 + AL2
        count = 2

    residual_fracture_surface_measured = total_sum / count
    return residual_fracture_surface_measured

def get_actual_stress_measured(F, residual_fracture_surface_measured):
    # Convert F and residual_fracture_surface_measured to float, handle non-numeric values
    F = convert_to_float(F)
    residual_fracture_surface_measured = convert_to_float(residual_fracture_surface_measured)

    if F is None:
        return None
    elif F == 0:
        return None
    elif residual_fracture_surface_measured == 0:
        return None
    else:
        actual_stress_measured = F / residual_fracture_surface_measured
        return actual_stress_measured
