import pandas as pd

def save_data(data: pd.DataFrame, file_path: str) -> None:
    """
    Save a pandas DataFrame to a CSV file.

    Args:
        data (pd.DataFrame): The DataFrame to be saved.
        file_path (str): The path where the CSV file will be saved.
    
    Raises:
        IOError: If there is an issue writing to the file.
    """
    try:
        data.to_csv(file_path, index=False)
        print(f"Data successfully saved to '{file_path}'.")
    except IOError as e:
        print(f"Error: Could not write to file '{file_path}'.")
        raise e