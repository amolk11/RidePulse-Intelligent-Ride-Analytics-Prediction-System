import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.
    
    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.
    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file cannot be parsed as a CSV.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: The file '{file_path}' was not found.")
        raise e
    except pd.errors.EmptyDataError as e:
        print(f"Error: The file '{file_path}' is empty.")
        raise e
    except pd.errors.ParserError as e:
        print(f"Error: The file '{file_path}' could not be parsed as a CSV.")
        raise e
    